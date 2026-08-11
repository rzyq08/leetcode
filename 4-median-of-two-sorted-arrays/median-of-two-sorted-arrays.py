class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        nums1.extend(nums2)
        nums1 = sorted(nums1)
        length = len(nums1)

        if length % 2 == 1:
            return float(nums1[length//2])
        else:
            return float((nums1[(length//2) - 1] + nums1[length//2]) / 2.0)