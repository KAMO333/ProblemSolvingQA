def is_armstrong_number(number):
    
    digits = [int(n) for n in str(number)]
    number_of_digits = len(digits)

    results = []

    for num in digits:
        power_up = pow(int(num), number_of_digits)
        results.append(power_up)

    summation = sum(results)


    return summation == number

