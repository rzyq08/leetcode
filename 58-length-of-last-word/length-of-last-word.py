class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        res = ""
        i = 0
        while i < len(s):
            if s[i] == ' ':
                res = ""
            else:
                res += s[i]
            i+=1
        return len(res)