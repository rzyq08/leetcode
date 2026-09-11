class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        count = {}
        for num in arr:
            count[num] = count.get(num, 0) + 1
        
        res = []
        for key,val in count.items():
            if val in res:
                return False
            res.append(val)
        return True