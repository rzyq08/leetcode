class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        hashm = {}
        for num in nums:
            hashm[num] = hashm.get(num, 0) + 1
        
        res = []
        for i in range(1, len(nums)+1):
            if i not in hashm:
                res.append(i)
        return res