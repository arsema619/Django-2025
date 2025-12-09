def two_sum(nums, target):
    # Dictionary to remember number -> index
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    # If no solution (though problem assumes exactly one), could return None or raise error
    return None

# Examples:
print(two_sum([2,7,11,15], 9))  # [0, 1]
print(two_sum([3,2,4], 6))      # [1, 2]
