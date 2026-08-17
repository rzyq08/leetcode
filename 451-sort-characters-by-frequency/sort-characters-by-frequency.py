class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = {}
        for let in s:
            count[let] = count.get(let, 0) + 1
        buckets = [[] for _ in range(len(s)+1)]

        for key,val in count.items():
            buckets[val].append(key*val)

        res = []
        for i in range(len(buckets)-1, -1, -1):
            for item in buckets[i]:
                res.append(item)
        return ''.join(res)