class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """

        try:
            if s.lower() in ("inf", "+inf", "-inf", "infinity", "+infinity", "-infinity", "nan"):
                return False
            else:
                float(s)
                return True
        except ValueError:
            return False