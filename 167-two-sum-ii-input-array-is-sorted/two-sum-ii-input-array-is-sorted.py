class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(numbers)
        l = 0
        r = length - 1
        while l < r:
            sm = numbers[l] + numbers[r]
            if sm == target:
                return [l+1, r+1]
            elif sm > target:
                r-=1
            elif sm < target:
                l+=1