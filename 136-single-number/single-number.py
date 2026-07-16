class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        hashm = Counter(nums)
        
        for x in hashm:
            if hashm[x] == 1:
                return x