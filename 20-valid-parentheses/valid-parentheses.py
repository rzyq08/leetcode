class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        par = {")":"(", "}":"{", "]":"["}
        curr = []

        for c in s:
            if c in par:
                if len(curr)!=0:
                    if curr[-1] == par[c]:
                        curr.pop()
                    else:
                        return False
                else:
                    return False
            else:
                curr.append(c)
        if len(curr)!=0:
            return False
        return True