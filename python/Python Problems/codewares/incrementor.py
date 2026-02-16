def incrementer(nums: list[int]) -> list[int]:
    results = []

    for number, index in enumerate(nums, start=1):
        add_numbers = number + index

        string_list = [num for num in str(add_numbers)]

        if len(string_list) == 1:
            convert_back_to_int = int("".join(str(add_numbers)))
            results.append(convert_back_to_int)
        else:
            last_number = int(string_list[-1])
            results.append(last_number)   

    return results

    # Big-O =  O(n^2)


print(incrementer([]), [])
print(incrementer([1, 2, 3]), [2, 4, 6])
print(incrementer([4, 6, 7, 1, 3]), [5, 8, 0, 5, 8])