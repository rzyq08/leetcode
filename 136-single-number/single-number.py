class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        hashm = {}
        for num in nums:
            hashm[num] = hashm.get(num, 0) + 1
        
        for x in hashm:
            if hashm[x] == 1:
                return x