class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mn = abs(min(nums))
        mx = abs(max(nums))

        while mn!=0:
            mx, mn = mn, mx%mn
        
        return mx