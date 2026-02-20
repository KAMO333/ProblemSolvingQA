def no_boring_zeros(n):
    # your code

    while n % 10 == 0 and n != 0:
        n = n // 10
    return n


print(no_boring_zeros(1450), 145)
print(no_boring_zeros(960000), 96)
print(no_boring_zeros(1050), 105)
