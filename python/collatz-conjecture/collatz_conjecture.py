def steps(number):
    
    if number < 1:
        raise ValueError("Only positive integers are allowed")
    
    steps_count = 0

    while number != 1:
        
        number = (number * 3) + 1 if number % 2 != 0 else number // 2
        steps_count += 1

    return steps_count
