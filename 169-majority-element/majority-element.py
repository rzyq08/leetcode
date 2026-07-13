class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        res = major = 0
        for num in nums:
            if major == 0:
                res = num
            
            major += 1 if num == res else -1
        return res