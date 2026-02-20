def find_longest(arr):
    results = {}

    for number in arr:
        results[number] = len(str(number))

    def get_score(item):
        return item[1]

    maximum = max(results.items(), key=get_score)

    return maximum[0]


print(find_longest([1, 10, 100]), 100)
print(find_longest([9000, 8, 800]), 9000)
print(find_longest([8, 900, 500]), 900)
print(find_longest([3, 40000, 100]), 40000)
