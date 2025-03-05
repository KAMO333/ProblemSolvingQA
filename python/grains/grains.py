def generate_chessboard_dict():    
    chessboard = {}

    for i in range(1, 65):
        chessboard[i] = 2**(i-1)

    return chessboard

def square(number):
    
    if number <= 0 or number > 64:
        raise ValueError("square must be between 1 and 64")
    
    for key, value in generate_chessboard_dict().items():
        if key == number:
            return value
        
def total():
    return sum(generate_chessboard_dict().values())

    
