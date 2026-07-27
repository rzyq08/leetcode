class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        isneg = False
        if x < 0:
            isneg = True
            x *= -1

        res = 0
        while x>0:
            res = (res*10)+(x%10)
            x//=10

        if res > 2**31 - 1:
            return 0
        
        if isneg == True:
            res*=-1
        return res