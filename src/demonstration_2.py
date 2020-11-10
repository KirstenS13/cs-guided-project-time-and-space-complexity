"""
Given a list of integers, your function should return `True` if any value
appears at least two times in the array. Your function should return `False` if
every element is unique.

Example:

Input: [1,3,3,2,1]
Output: True

Example:

Input: [0,1,2,3]
Output: False

*Note: In your first solution, it is okay to use a simple linear search. What
is the time complexity of this approach? Other possible solutions will have
time complexities of `O(n log n)` or `O(n)`. Possible space complexities are
`O(1)` or `O(n)`. Try to come up with solutions with different time and space
complexities and think about the tradeoffs between the solutions.*
"""
def contains_duplicate(nums):
    # Plan1:
    # nums_set = set(nums)
    # if len(nums_set) == len(nums):
    #     return False
    # else:
    #     return True

    # made a set
    # if set length wasn't equal to the original array length: that means there were duplicates
    # Runtime: O(n)
    # Space: O(n)

    # Plan2:
    # i = 0
    # while i < len(nums) - 1:
    #     if nums[1] == nums[i+1]:
    #         return True
    #     i += 1
    # return False

    # This assumes that nums is sorted
    # simply add nums.sort() before i = 0
    # runtime: O(n log n) bc sorting is usually O(n log n)
    # space: O(1)