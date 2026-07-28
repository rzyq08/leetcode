class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num = set(nums)
        mx = 0
        for nm in num:
            if nm-1 not in num:
                count = 0
                while nm+count in num:
                    count+=1
                mx = max(mx, count)
        return mx