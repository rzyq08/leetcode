class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        count = {}
        for word in words:
            count[word] = count.get(word, 0) + 1
        
        bucket = [[] for _ in range(len(words)+1)]
        for key,val in count.items():
            bucket[val].append(key)
        
        res = []
        for i in range(len(bucket)-1,-1,-1):
            bucket[i].sort()
            for item in bucket[i]:
                res.append(item)
                if len(res)==k:
                    return res