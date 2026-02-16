def get_middle(s):

    mid_index = len(s) // 2

    if len(s) % 2 == 0:
        return s[mid_index - 1: mid_index + 1]
    else:
        return s[mid_index]
        




print(get_middle("test"),"es")
print(get_middle("testing"),"t")
print(get_middle("middle"),"dd")
print(get_middle("A"),"A")
print(get_middle("of"),"of")