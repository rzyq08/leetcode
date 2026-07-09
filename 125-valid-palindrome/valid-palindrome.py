class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        before = [let.lower() for let in s if let.isalnum() == True]
        lst = [let.lower() for let in s if let.isalnum() == True]

        left = 0
        right = len(lst)-1
        while left < right:
            lst[left], lst[right] = lst[right], lst[left]
            left+=1
            right-=1
        return lst == before