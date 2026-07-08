class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numset = set(nums)
        res = 0

        for num in numset:
            if num-1 not in numset:
                count = 0
                while num+count in numset:
                    count+=1
                res = max(count, res)
        return res