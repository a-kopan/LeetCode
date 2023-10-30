def isAnagram(s,t):
    sA = list(s)
    tA = list(t)
    sA.sort()
    tA.sort()
    return sA==tA

print(isAnagram("rat","car"))