class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mx = 0
        for i in range(1, min(nums)+1):
            if max(nums) % i == 0 and min(nums) % i == 0:
                mx = max(mx, i)
        return mx