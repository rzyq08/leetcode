class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numset = defaultdict(int)
        res = 0

        for num in nums:
            if numset[num] == 0:
                numset[num] = numset[num-1] + numset[num+1] + 1
                numset[num - numset[num-1]] = numset[num]
                numset[num + numset[num+1]] = numset[num]
                res = max(res, numset[num])
        return res 