class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = set(nums)
        return [i for i in range(min(nums), max(nums)) if i not in nums]