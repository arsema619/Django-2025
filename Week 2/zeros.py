
def move_zeroes(nums):
    insert_pos = 0
    for num in nums:
        if num != 0:
            nums[insert_pos] = num
            insert_pos += 1
    while insert_pos < len(nums):
        nums[insert_pos] = 0
        insert_pos += 1

# Input from user
nums = input("Enter numbers separated by space: ").split()
nums = [int(x) for x in nums]  # Convert to integers

move_zeroes(nums)
print("After moving zeros:", nums)
