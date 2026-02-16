def crap(garden: list[list[str]], bags: int, cap: int) -> str:
    number_of_crap = 0
    total_space = bags * cap

    for garden_space in garden:
        for garden_pick in garden_space:
            if garden_pick == "D":
                return "Dog!!"
            
            if garden_pick == "@":
                number_of_crap += 1

    if number_of_crap <= total_space:
        return "Clean"
    else:
        return "Cr@p"
        



print(crap([['_','_','_','_'], ['_','_','_','@'], ['_','_','@', '_']], 2, 2), "Clean")
print(crap([['_','_','_','_'], ['_','_','_','@'], ['_','_','@', '_']], 1, 1), "Cr@p")
print(crap([['_','_'], ['_','@'], ['D','_']], 2, 2), "Dog!!" )
