def is_happy(n: int) -> bool:
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        total = 0
        while n > 0:
            n, digit = divmod(n, 10)
            total += digit * digit
        n = total
    return n == 1
