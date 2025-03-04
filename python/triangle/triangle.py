def greater_than_zero_sides(sides):
    if sides[0] and sides[1] and sides[2] > 0: 
        return True
    return False

def sum_of_two(sides):
    first_two = sides[0] + sides[1]
    second_and_last = sides[1] + sides[2]
    first_and_last = sides[0] + sides[2]

    return first_two >= sides[2] and second_and_last >= sides[0] and first_and_last >= sides[1]
        

def equilateral(sides):
    
    if greater_than_zero_sides(sides) and sum_of_two(sides):
        if sides[0] == sides[1] and sides[0] == sides[2]:
            return True
        return False
    return False




def isosceles(sides):
    pass


def scalene(sides):
    pass
