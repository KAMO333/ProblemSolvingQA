class List:
    def remove_(self, integer_list, values_list):
        results = []

        for number in integer_list:
            if number not in values_list:
                results.append(number)

        return results

        #   Big-O = O(n)


check_list = List()
integer_list = [1, 1, 2, 3, 1, 2, 3, 4]
values_list = [1, 3]
print(check_list.remove_(integer_list, values_list), [2, 2, 4])
