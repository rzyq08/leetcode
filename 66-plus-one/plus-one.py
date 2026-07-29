class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digit = ''.join(str(digit) for digit in digits)
        res = int(digit) + 1
        return [int(num) for num in str(res)]