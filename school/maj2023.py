def count_blocks(n):
    if n <= 0:
        return 0
    prev = n % 2
    print(f"prev: {prev}")
    b = 1
    print(f"b: {b}")
    n = n // 2
    print(f"n po pierwszym dzieleniu: {n}")
    while n > 0:
        print(f"n w while: {n}")
        curr = n % 2
        print(f"curr: {curr}")
        if curr != prev:
            b += 1
            prev = curr
            print(f"b po inkrementacji: {b}")
            print(f"prev po aktualizacji: {prev}")
        n = n // 2
    return b
print("------------0------------")
print(count_blocks(0))
print("------------67------------")
print(count_blocks(67))
print("------------245------------")
print(count_blocks(245))