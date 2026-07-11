class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lst = [let.lower() for let in s if let.isalnum() == True]

        s = ''.join(lst)

        return s == s[::-1]