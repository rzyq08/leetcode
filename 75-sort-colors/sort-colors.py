class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            b = i
            while b > 0 and nums[b-1] > nums[b]:
                nums[b-1], nums[b] = nums[b], nums[b-1]
                b-=1