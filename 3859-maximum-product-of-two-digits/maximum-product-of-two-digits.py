class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = [int(num) for num in str(n)]
        mx = 0
        for i in range(len(n)):
            for j in range(i+1, len(n)):
                prod = n[i]*n[j]
                mx = max(mx, prod)
        return mx