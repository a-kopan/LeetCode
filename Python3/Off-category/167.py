    # I (works worse with multiple same elements at the beggining/end)
    #go from the right, and compare the most-right element with the lower ones as long
    #as they don't exceed the target
    
    # II (works worse if there are a lot of unique elements)
    #create a hashmap for each element that stores the array of indecies, and then compare the keys only

    # III create a set of elements from the array, and then go over the values inside the set to check for sum
    #if there is none, then check duplicates of elements from the set.
def twoSum(nums,target):
    r=len(nums)-1
    #set right bound to first number from the right that's not bigger than target
    for i in range(r,-1,-1):
        if abs(nums[i])<=abs(target):
            r=i
            break
    """
    #version I (TIME LIMIT EXCEEDED)
    for j in range(r,-1,-1):
        for i in range(0,r):
            if nums[i]+nums[j]==target:
                return [i+1,j+1]
            elif nums[i]+nums[j]>target:
                break
    """
    #version II
    indexMap = dict()
    for i, val in enumerate(nums):
        indexMap.setdefault(val,[])
        indexMap[val].append(i)
    #now compare each key with the target and then get the earliest index of te values
    for key1 in indexMap.keys():
        for key2 in indexMap.keys():
            if key1+key2==target and key1!=key2 :
                indecies = (indexMap[key1][0],indexMap[key2][0])
                return [min(indecies)+1,max(indecies)+1]
            elif key1==key2 and key1+key2==target and len(indexMap[key1])>1:
                indecies = (indexMap[key1][0],indexMap[key2][1])
                return [min(indecies)+1,max(indecies)+1]
    
t1 = ([2,7,11,15],9)
t2 = ([2,3,4],6)
t3 = ([-1,0],-1)

tests = [t1,t2,t3]
[print(x,": ",twoSum(x[0],x[1])) for x in tests]