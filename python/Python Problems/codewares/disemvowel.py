def disemvowel(string: str) -> str:
    vowels_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    results = [char for char in string if char not in vowels_list]

    return "".join(map(str, results))



print(disemvowel("This website is for losers LOL!"), "Ths wbst s fr lsrs LL!")