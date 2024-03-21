from functools import cmp_to_key


def compare_absolute(x, y):
    return abs(x[0]) - abs(y[0])
    # compare determined by the absolute value of first element of the tuple


numbers = [(1, 2), (-2, 4), (-3, 5), (1, 1)]
sorted_numbers = sorted(numbers, key=cmp_to_key(compare_absolute))

print(sorted_numbers)  # [1, 3, 6, 9]
