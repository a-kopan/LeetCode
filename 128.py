def longestConsecutive(nums):
    if len(nums)==0:
        return 0
    nums = list(set(nums))
    nums.sort()
    temp_count = 1
    biggest_count = 0
    for ind in range(1,len(nums)):
        if nums[ind]==nums[ind-1]+1: #or nums[ind]==nums[ind-1]:
            temp_count+=1
        else:
            if biggest_count<temp_count:
                biggest_count=temp_count
            temp_count=1
    if temp_count>biggest_count:
        return temp_count
    return biggest_count


t1 = [100,4,200,1,3,2]
t2 = [0,3,7,2,5,8,4,6,0,1]
t3 = [0,-1]
t4 = [0]
t5 = []
tests = [t1,t2,t3,t4,t5]
[print(x,": ",longestConsecutive(x)) for x in tests]