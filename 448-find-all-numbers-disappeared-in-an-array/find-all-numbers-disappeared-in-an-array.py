class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            now = abs(nums[i]) - 1
            if nums[now] > 0:
                nums[now] *= -1
        
        return [i+1 for i in range(len(nums)) if nums[i] > 0]