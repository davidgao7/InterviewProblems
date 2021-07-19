def reverse_better(self, x: int) -> int:
    y, res = abs(x), 0
    # 则其数值范围为 [−2^31,  2^31 − 1]
    boundry = (1 << 31) - 1 if x > 0 else 1 << 31
    while y != 0:
        res = res * 10 + y % 10
        if res > boundry:
            return 0
        y //= 10
    return res if x > 0 else -res
# using binary shifting for one line boundary condition without calculating
