class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        prefix = [1]*(length+1)
        postfix = [1]*(length+1)

        prefix[1] = nums[0]
        for i in range(1, length):
            prefix[i+1] = prefix[i]*nums[i]
        for i in range(length-1, -1, -1):
            postfix[i] = nums[i]*postfix[i+1]
        
        res = [1]*length
        for i in range(1, length+1):
            res[i-1] = prefix[i-1]*postfix[i]
        return res