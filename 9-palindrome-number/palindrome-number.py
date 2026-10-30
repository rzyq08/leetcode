class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        try:
            strx = str(x)
            if x == int(strx[::-1]):
                return True
            else:
                return False
        except ValueError:
            return False