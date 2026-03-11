"""mvcc_mental_model - a tiny snapshot-visibility model."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class RowVersion:
    value: object
    created_xid: int
    deleted_xid: int | None = None


VersionedStore = dict[str, list[RowVersion]]


def append_version(
    store: VersionedStore,
    key: str,
    value: object,
    created_xid: int,
) -> None:
    store.setdefault(key, []).append(
        RowVersion(value=value, created_xid=created_xid)
    )


def replace_visible_value(
    store: VersionedStore,
    key: str,
    new_value: object,
    writer_xid: int,
) -> None:
    versions = store.setdefault(key, [])
    current = next(
        (version for version in reversed(versions) if version.deleted_xid is None),
        None,
    )
    if current is not None:
        current.deleted_xid = writer_xid
    versions.append(RowVersion(value=new_value, created_xid=writer_xid))


def delete_visible_value(
    store: VersionedStore,
    key: str,
    writer_xid: int,
) -> None:
    versions = store.get(key, [])
    current = next(
        (version for version in reversed(versions) if version.deleted_xid is None),
        None,
    )
    if current is not None:
        current.deleted_xid = writer_xid


def visible_value(
    store: VersionedStore,
    key: str,
    snapshot_xid: int,
) -> object | None:
    versions = store.get(key, [])
    visible_versions = [
        version
        for version in versions
        if version.created_xid <= snapshot_xid
        and (version.deleted_xid is None or version.deleted_xid > snapshot_xid)
    ]
    if not visible_versions:
        return None
    return visible_versions[-1].value
