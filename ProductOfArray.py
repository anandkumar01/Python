# Return the product of all integers of the array except itself

def product_except_self(nums):
    k = 1
    temp = []
    for i in range(len(nums)):
        temp.append(k)
        k = k * nums[i]
    k = 1  # re assign k=1
    for i in range(len(nums) - 1, -1, -1):
        temp[i] *= k
        k *= nums[i]
    return temp


nums = [1, 2, 3, 4]
print(product_except_self(nums))
