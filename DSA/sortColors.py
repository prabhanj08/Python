"""
Given an array nums with n objects colored red, white, or blue, sort them inplace so that objects of the same color are adjacent, with the colors in the
order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue,
respectively.
You must solve this problem without using the library's sort function.
Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

"""


#############################################
"""
DNF Algorithm
The problem was posed with three colors, here `0′, `1′ and `2′. The array is divided into four sections: 
arr[1] to arr[low – 1]
arr[low] to arr[mid – 1]
arr[mid] to arr[high – 1]
arr[high] to arr[n]
If the ith element is 0 then swap the element to the low range.
Similarly, if the element is 1 then keep it as it is.
If the element is 2 then swap it with an element in high range.

*** 

Keep three indices low = 1, mid = 1, and high = N and there are four ranges, 1 to low (the range containing 0), low to mid (the range containing 1), mid to high (the range containing unknown elements) and high to N (the range containing 2).
Traverse the array from start to end and mid is less than high. (Loop counter is i)
If the element is 0 then swap the element with the element at index low and update low = low + 1 and mid = mid + 1
If the element is 1 then update mid = mid + 1
If the element is 2 then swap the element with the element at index high and update high = high – 1 and update i = i – 1. As the swapped element is not processed
Print the array.
"""

def sortColors(nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        low = 0
        mid = 0
        high = len(nums)-1
        while mid <= high:
            print(mid,high)
            print(nums)
            if nums[mid] == 0:
                print("mid eq to 0")
                nums[mid] = nums[low]
                nums[low] = 0
                low += 1
                mid += 1
            elif nums[mid] == 2:
                print("mid eq to 2")
                nums[mid] = nums[high]
                nums[high] = 2
                high -= 1
            else:
                print("mid eq to 1")
                mid += 1
        return nums
print(sortColors([1,2,0,2,1,1,0]))