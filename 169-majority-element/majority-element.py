class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = defaultdict(int)

        for num in nums:
            a[num] += 1

        for key, val in a.items():
            if val > len(nums)//2:
                return key
