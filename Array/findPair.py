"""
# How do you find all pairs of an integer array whose sum is equal to a given number
# A = [1,2,3,4,5,6,7]

# input = 5
# output = 1,4,2,3

"""

# Brute-Force
def findPair(nums, target):
    # consider each element except the last
    keys = []
    for i in range(len(nums) - 1):

        # start from the i'th element until the last element
        for j in range(i + 1, len(nums)):

            # if the desired sum is found, print it
            if nums[i] + nums[j] == target:
               # print('Pair found', (nums[i], nums[j]))
                keys.append([nums[i], nums[j]])
    return keys

    # No pair with the given sum exists in the list
    print('Pair not found')


if __name__ == '__main__':
    nums = [7,8, 1, 3, 2, 5, 1,7]
    target = 10

    print("Brute Force result : ", findPair(nums, target))



# Using Sorting

# Function to find a pair in an array with a given sum using sorting
def findPairSort(nums, target):
    # sort the list in ascending order
    sortkeys = []
    nums.sort()

    # maintain two indices pointing to endpoints of the list
    (low, high) = (0, len(nums) - 1)

    # reduce the search space `nums[low…high]` at each iteration of the loop

    # loop till the search space is exhausted
    while low < high:

        if nums[low] + nums[high] == target:  # target found
           # print('Pair found', (nums[low], nums[high]))
            sortkeys.append((nums[low], nums[high]))
            #return

        # increment `low` index if the total is less than the desired sum;
        # decrement `high` index if the total is more than the desired sum
        if nums[low] + nums[high] < target:
            low = low + 1
        else:
            high = high - 1
    return sortkeys

    # No pair with the given sum exists
    print('Pair not found')


if __name__ == '__main__':
    nums = [7,8, 1, 3, 2, 5, 1,7]
    target = 10

    print("Sorting Result : ", findPairSort(nums, target))


# Hashing

# Function to find a pair in an array with a given sum using hashing
def findPairHash(nums, target):
    # create an empty dictionary
    d = {}
    hashkeys = []

    # do for each element
    for i, e in enumerate(nums):

        # check if pair (e, target - e) exists

        # if the difference is seen before, print the pair
        if target - e in d:
            #print('Pair found', (nums[d.get(target - e)], nums[i]))
            hashkeys.append((nums[d.get(target - e)], nums[i]))


        # store index of the current element in the dictionary
        d[e] = i
    return hashkeys
    # No pair with the given sum exists in the list
    print('Pair not found')


if __name__ == '__main__':
    nums = [7,8, 1, 3, 2, 5, 1,7]
    target = 10

    print("Hash result : ",findPairHash(nums, target))