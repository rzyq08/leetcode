class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 1 and nums[0]+1 == target:
            return 1
        elif target in nums:
            return nums.index(target)
        elif len(nums) == 1:
            return 0
        elif target > max(nums):
            return nums.index(max(nums)) + 1
        elif target < min(nums):
            return 0
        else:
            for i, num in enumerate(nums):
                if num+1 == target:
                    return i+1
                elif num-1 == target:
                    return i
        