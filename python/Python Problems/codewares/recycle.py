def recycle_me(rubbish):
    plastic = 0
    glass = 0
    card = 0

    for item in rubbish:
        if item > 0:
            plastic += 1
        if item < 0:
            glass += 1
        if item == 0:
            card += 1

    return (plastic, glass, card)


print(recycle_me([5, -9, 0, 6, -84, -95, 15]), (3, 3, 1))
print(recycle_me([45, -26, -4, -66, -84, -38, 14]), (2, 5, 0))
