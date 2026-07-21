class Solution(object):
    def sumOfUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashm = {}
        for num in nums:
            hashm[num] = hashm.get(num, 0) + 1
        
        res = 0
        for key,val in hashm.items():
            if val == 1:
                res+=key
        return res