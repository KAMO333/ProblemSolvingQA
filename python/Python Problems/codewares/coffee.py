from typing import Union

def how_much_coffee(events: list) -> Union[int, str]:
    accepted_events = ['cw', 'cat', 'dog', 'movie', 'CW', 'CAT', 'DOG', 'MOVIE']
    coffees = 0


    for event in events:
        check_accepted_events = event in accepted_events

        if event == event.upper() and check_accepted_events:
            coffees += 2
        elif event == event.lower() and check_accepted_events:
            coffees += 1

    return "You need extra sleep" if coffees > 3 else coffees

# Big-O = O(n) 


print(how_much_coffee([]), 0)
print(how_much_coffee(['cw']), 1)
print(how_much_coffee(['CW']), 2)
print(how_much_coffee(['cw','CAT']), 3)
print(how_much_coffee(['cw','CAT','DOG']), 'You need extra sleep')
print(how_much_coffee(['cw','CAT', 'cw=others']), 3)