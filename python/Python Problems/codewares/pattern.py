def pattern(n: int) -> str:

    if n <= 0:
        return ""

    final_pattern = ""

    pattern_results = []

    for number in range(1, n + 1):
        pattern_results.append(number)

    print("check ", pattern_results)

    number_to_check = n

    print(number_to_check)

    data = pattern_results.splitlines()

    print("data ", data)

    # last_row = data[-1]

    # match_with = last_row[0]

    # final_pattern += pattern_results + "\n"

    # while number_to_check != match_with:
    #     the_rest = last_row[1:] + match_with

    #     final_pattern += the_rest + "\n"

    #     last_row = the_rest
    #     match_with = last_row[0]

    # return final_pattern


print(pattern(11))
# "1234567891011\n"
# "2345678910111\n"
# "3456789101112\n"
# "4567891011123\n"
# "5678910111234\n"
# "6789101112345\n"
# "7891011123456\n"
# "8910111234567\n"
# "9101112345678\n"
# "1011123456789\n"
# "1112345678910",
