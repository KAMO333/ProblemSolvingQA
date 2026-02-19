def scramble(strng, array):

    results = []

    while len(results) < len(array):
        results.append(None)

    for i in range(len(strng)):
        results[array[i]] = strng[i]

    return "".join(results)


print(scramble("abcd", [0, 3, 1, 2]), "acbd")
print(scramble("sc301s", [4, 0, 3, 1, 5, 2]), "c0s3s1")
print(scramble("bskl5", [2, 1, 4, 3, 0]), "5sblk")
