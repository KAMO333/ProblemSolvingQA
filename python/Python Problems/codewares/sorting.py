def solution(nums):
    if type(nums) == list and len(nums) >= 1:
        nums.sort()
        return nums
    else:
        return []



print(solution([1,2,3,10,5]), [1,2,3,5,10])
print(solution(None), [])
print(solution([]), [])
print(solution([20,2,10]), [2,10,20])
print(solution([2,20,10]), [2,10,20])
print(solution([-31]), [-31])