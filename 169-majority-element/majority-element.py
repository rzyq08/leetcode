class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = Counter(nums)

        for key,val in a.items():
            if val > (len(nums)/2):
                return key
