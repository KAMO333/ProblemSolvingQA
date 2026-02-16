def accum(st: str) -> str:
    results = ""

    for index, char in enumerate(st, start=1):
        multiple_char = char * index
        make_upper_case = multiple_char.capitalize()
        results += f"{make_upper_case}{'-'}"

    return results[:-1]
        



print(accum("ZpglnRxqenU"), "Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu")
print(accum("NyffsGeyylB"), "N-Yy-Fff-Ffff-Sssss-Gggggg-Eeeeeee-Yyyyyyyy-Yyyyyyyyy-Llllllllll-Bbbbbbbbbbb")