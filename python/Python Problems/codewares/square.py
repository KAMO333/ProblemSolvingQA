def square_digits(num: int):

    result = []

    digits = [int(number) for number in str(num)]

    for usable_number in digits:
        result.append(usable_number * usable_number)

    return int("".join(str(i) for i in result))

    


print(square_digits(9119), 811181)
print(square_digits(0), 0)