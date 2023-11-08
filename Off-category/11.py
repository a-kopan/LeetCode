def maxArea(height) -> int:
    max_area = 0
    l = 0
    r = len(height)-1
    while l<r:
        temp_area = abs(l-r)*min(height[l],height[r])
        if temp_area > max_area: max_area = temp_area
        if height[l]>height[r]: r-=1
        else: l+=1
    return max_area