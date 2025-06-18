def count_rotations(nums):
    lo = 0
    hi = len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        mid_num = nums[mid]

        if mid > 0 and mid_num < nums[mid - 1]:
            return mid
        elif mid_num > hi:
            hi = mid -1
        else :
            lo = mid + 1
    return 0


nums = []
n = int(input("No. of elements you want to enter = "))
for i in range(n) :
    nums.append(int(input()))

print(count_rotations(nums))
