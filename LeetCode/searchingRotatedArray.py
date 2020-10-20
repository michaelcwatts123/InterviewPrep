# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

# You are given a target value to search. If found in the array return true, otherwise return false.
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        nums = list(set(nums))
        nums = {n: '' for n in nums}
        if target in nums.keys():
            return True
        else:
            return False