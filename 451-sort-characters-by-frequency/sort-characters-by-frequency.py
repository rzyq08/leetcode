class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = Counter(s)
        
        buckets = [[] for _ in range(len(s)+1)]
        for key,val in count.items():
            buckets[val].append(key)

        res = []
        for i in range(len(buckets)-1, 0, -1):
            for item in buckets[i]:
                res.append(item*i)
        return ''.join(res)