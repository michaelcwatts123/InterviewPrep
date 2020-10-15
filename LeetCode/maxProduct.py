# Given an integer array, find three numbers whose product is maximum and output the maximum product.

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if(max(nums) < 0 or min(nums) >= 0):
            total = max(nums)
            nums[nums.index(total)] = -sys.maxsize
            for i in range(2):
                total *= max(nums)
                nums[nums.index(max(nums))] = -sys.maxsize
            return total
        else:
            min1 = min(nums)
            nums[nums.index(min1)] = 0
            min2 = min(nums)
            nums[nums.index(min2)] = 0
            maxNum = max(nums)
            nums[nums.index(maxNum)] = 0
            max1 = max(nums)
            nums[nums.index(max1)] = 0
            max2 = max(nums)
            nums[nums.index(max2)] = 0
            if((min1*min2) > (max1*max2)):
                return (min1*min2*maxNum)
            else:
                return (maxNum*max1*max2)