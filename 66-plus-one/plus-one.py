class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        #digit = int(''.join(str(digit) for digit in digits)) + 1
        return [int(num) for num in str(int(''.join(str(digit) for digit in digits)) + 1)]