def threeSum(nums):
    nums.sort()
    l=0
    r=len(nums)
    
    while l<r:
        a=0
t1 = [-1,0,1,2,-1,-4]
t2 = [1,2,-2,-1]
#t3 = [0,-1]
#t4 = [0]
#t5 = []
tests = [t1,t2]#,t3,t4,t5]
[print(x,": ",threeSum(x)) for x in tests]