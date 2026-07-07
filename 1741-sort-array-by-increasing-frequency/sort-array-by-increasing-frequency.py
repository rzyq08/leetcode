class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        res = [[] for i in range(len(nums)+1)]
        for key,val in count.items():
            res[val].append(key)
        
        result = []
        for num in res:
            num = sorted(num)
            num.reverse()
            for i in range(len(num)):
                result.extend([num[i]]*count[num[i]])
        return result