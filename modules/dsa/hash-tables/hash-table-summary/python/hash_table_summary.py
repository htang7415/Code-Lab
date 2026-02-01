def hash_table_summary(values: list[str]) -> dict[str, int | str | None]:
    if not values:
        return {"unique": 0, "most_common": None, "max_count": 0}

    counts: dict[str, int] = {}
    for value in values:
        counts[value] = counts.get(value, 0) + 1

    most_common = None
    max_count = 0
    for key in sorted(counts):
        count = counts[key]
        if count > max_count:
            max_count = count
            most_common = key
    return {"unique": len(counts), "most_common": most_common, "max_count": max_count}
