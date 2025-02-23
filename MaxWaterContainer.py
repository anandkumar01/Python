def max_water_container(nums):
    n = len(nums)
    left, right = 0, n - 1
    maxArea = 0
    
    while left < right:
        width = right - left
        hight = min(nums[left], nums[right])
        curArea = width * hight
        maxArea = max(curArea, maxArea)
        if nums[left] < nums[right]:
            left += 1
        else:
            right -= 1
    return maxArea


nums = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(max_water_container(nums))
