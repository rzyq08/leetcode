class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashm = Counter(nums)
        
        for key, val in hashm.items():
            if val > 1:
                return key