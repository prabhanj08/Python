"""
    Find First and Last Position of Element in Sorted Array
    Given an array of integers nums sorted in non-decreasing order, find the
    starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.
Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
"""


def searchRange(nums, target):
    if nums.count(target) != 0:
        first_place = nums.index(target)
        return [first_place, (first_place + nums.count(target) - 1)]
    return [-1, -1]


#print(searchRange([5,7,7,8,8,8,10],8))


def searchRange(nums, target):
        def search(x):
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = (lo + hi) // 2
                if nums[mid] < x:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        lo = search(target)
        hi = search(target + 1) - 1

        if lo <= hi:
            return [lo, hi]

        return [-1, -1]

print(searchRange([5,7,7,8,8,8,10],8))