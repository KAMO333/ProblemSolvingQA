def add(num1, num2):
    
    first = str(num1)
    second = str(num2)

    results = []

    longest = max(len(first), len(second))

    first = first.zfill(longest)
    second = second.zfill(longest)

    for number1, number2 in zip(first, second):
            results.append(int(number1) + int(number2))

    return int("".join(map(str, results)))



print(add(2,11), 13)
print(add(0,1), 1)
print(add(0,0), 0)


# print(add(16,18), 214)
# print(add(26,39), 515)
print(add(122,81), 1103)