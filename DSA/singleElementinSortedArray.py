"""
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.



Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10

"""

""" Solution 1"""
def singleelement(arr):
    low, high = 0, len(arr) - 1
    while low < high:
        mid = (low + high)//2
        if mid%2 == 1:
            mid -= 1

        if nums[mid] != nums[mid + 1]:
            high = mid
        else :
            low = mid + 2
    return nums[low]

nums = [1,1,2,3,3,4,4,8,8]
print(singleelement(nums))

""" Solution 2 """
def singleelement2(arr):
    return 2*sum(set(arr)) - sum(arr)

nums = [1,1,2,3,3,4,4,8,8]
print(singleelement2(nums))