def topKFrequent(nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hMap = dict()
        for i in nums:
            hMap.setdefault(i,0)
            hMap[i]+=1
        
        sortedTuples = sorted(hMap.items(), key=lambda x:x[1], reverse=True)[0:k]
        sortedHMap = dict(sortedTuples)
        return sortedHMap.keys()
test = ([-1,-1],1)
test2 = ([1,1,1,2,2,3],2)
print("For [-1,-1] and k=1: ",topKFrequent(test[0],test[1]))   
print("For [1,1,1,2,2,3] and k=2: ",topKFrequent(test2[0],test2[1]))   