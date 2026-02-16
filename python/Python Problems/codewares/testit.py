def testit(string: str) -> str:
    result = ""

    for letter in string:
        if letter.isalpha():
            result += letter.upper()
        else:
            result += letter

    return result



print(testit(""), "")
print(testit("a"), "A")
print(testit("b"), "B")
print(testit("a a"), "A A")
print(testit('AA'), 'aA')
print(testit('AB AB'), 'aB aB')