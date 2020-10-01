# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You may assume no duplicates in the array.

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        vals = nums
        offset = 0
        while(len(vals) > 2):
            if(vals[len(vals)//2] > target):
                vals = vals[0:len(vals)//2]
                print(vals)
            else:
                offsetVal = len(vals[:len(vals)//2])
                vals = vals[len(vals)//2:]
                offset = offsetVal + offset

        if(len(vals) == 1):
            if(vals[0] < target):
                return offset + 1
        if(vals[0] == target or vals[0] > target):
            return offset 
        if(vals[1] < target):
            return offset + 2
        else:
            return offset + 1
        