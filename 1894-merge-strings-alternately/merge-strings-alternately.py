class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        
        merge = []
        for a,b in zip(word1, word2):
            merge.append(a+b)
        merge.append(word1[len(word2):])
        merge.append(word2[len(word1):])
        return ''.join(merge)