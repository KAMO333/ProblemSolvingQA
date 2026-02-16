def only_one(*args: bool) -> bool:

    counter = 0

    for boolean in args:
        if boolean == True:
            counter += 1

    return True if counter == 1 else False 

    # Big-O = O(n)    
    
print(only_one(), False)
print(only_one(True, False), True)
print(only_one(False, False, False), False)
print(only_one(True, False, False, True), False)