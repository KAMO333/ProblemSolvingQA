def pickingNumbers(a):
    
    results = []


    for i in a:
        for j in a:
            if i != j:
                minus = j - i

                if minus == 0 or minus == 1:
                    results.append(i)

    print(results)
    return len(results)    
            


print(pickingNumbers([4 ,6 ,5 ,3 ,3 ,1]), 3)
# print(pickingNumbers([1 ,2 ,2 ,3 ,1 ,2]), 5)