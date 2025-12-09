def move_zeroes(nums):
    # pointer `last_non_zero_found_at` for the position to place next non-zero
    last_non_zero_found_at = 0

    # First pass: move non-zeroes forward
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[last_non_zero_found_at] = nums[i]
            last_non_zero_found_at += 1

    # Then fill remaining positions with zeros
    for i in range(last_non_zero_found_at, len(nums)):
        nums[i] = 0

# Examples:
arr1 = [0,1,0,3,12]
move_zeroes(arr1)
print(arr1)  # [1,3,12,0,0]

arr2 = [0]
move_zeroes(arr2)
print(arr2)  # [0]
