# Tenant Sharding Basics

> Track: `databases` | Topic: `nosql`

## Concept

Tenant sharding maps each tenant to a shard so the system can scale horizontally while keeping one tenant's data colocated.

## Key Points

- A stable routing function sends the same tenant to the same shard.
- Hash-based routing spreads normal tenants without a big lookup table.
- Large tenants often need explicit overrides because one hot tenant can dominate a shard.
- Routing logic should make both the default path and the override path obvious.

## Minimal Code Mental Model

```python
shard = default_shard("tenant-7", shard_count=4)
route = route_tenant("tenant-7", shard_count=4, overrides={"tenant-99": 3})
loads = shard_loads({"tenant-7": 10, "tenant-99": 500}, shard_count=4, overrides={"tenant-99": 3})
```

## Function

```python
def default_shard(tenant_id: str, shard_count: int) -> int:
def route_tenant(
    tenant_id: str,
    shard_count: int,
    overrides: dict[str, int] | None = None,
) -> int:
def shard_loads(
    tenant_sizes: dict[str, int],
    shard_count: int,
    overrides: dict[str, int] | None = None,
) -> dict[int, int]:
def hottest_shard(loads: dict[int, int]) -> int:
```

## Run tests

```bash
pytest modules/databases/nosql/tenant-sharding-basics/python -q
```
