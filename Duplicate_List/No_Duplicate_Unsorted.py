# Remove all duplicate elements from unsorted list
def remove_all_duplicates1(nums):
    return list(dict.fromkeys(nums))


# Using filter and lambda function
def remove_all_duplicates2(nums):
    visited = set()
    return list(filter(lambda x: x not in visited and not visited.add(x), nums))


def remove_all_duplicates3(nums):
    if not nums:
        return []

    visited = set()
    result = []
    for num in nums:
        if num not in visited:
            result.append(num)
            visited.add(num)
    return result


# Test the function
nums = [3, 4, 2, 5, 3, 6, 4, 7, 8]
print(remove_all_duplicates3(nums))
