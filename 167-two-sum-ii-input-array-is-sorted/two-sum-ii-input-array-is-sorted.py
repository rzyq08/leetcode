class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i, num in enumerate(numbers):
            pair = target - num
            if pair in seen:
                return [seen[pair]+1, i+1]

            seen[num] = i