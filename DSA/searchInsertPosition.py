"""
Given a sorted array of distinct integers and a target value, return the index if
the target is found. If not, return the index where it would be if it were inserted
in order.
You must write an algorithm with O(log n) runtime complexity.
Example 1:
Input: nums = [-1,0,3,5,9,12]
Output: 0

"""


def searchIndex(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1

        while left <= right:
            print(left, right)
            mid = (left + right) // 2
            print("mid", mid)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1

        return left



#print(searchIndex([-1,0,3,5,9,12],-5))

import bisect
def searchInsert(nums, target: int):
    return bisect.bisect_left(nums, target)

print(searchInsert([-1,0,3,5,9,12],5))