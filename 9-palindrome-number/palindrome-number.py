class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        n = str(x)

        l, r = 0, len(n)-1

        while l<r:
            if n[l]!=n[r]:
                return False
            l+=1
            r-=1
        return True