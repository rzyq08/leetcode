class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        sm = (length*(length+1))//2
        sm1 = sum(nums)
        return sm-sm1