class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        return [key for key,val in count.items() if val>1]