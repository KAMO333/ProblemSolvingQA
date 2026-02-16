def max_product(array: list) -> int:
    sorted_array = sorted(array, reverse=True)
    return sorted_array[0] * sorted_array[1]

# Big-O: O(n^2)

print(max_product([2, 1, 5, 0, 4, 3]), 20)
print(max_product([7, 8, 9]), 72)
print(max_product([33, 231, 454, 11, 9, 99, 57]), 104874)
