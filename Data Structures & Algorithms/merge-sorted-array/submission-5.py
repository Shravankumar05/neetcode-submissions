class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        tmp = nums1.copy()
        idx1, idx2 = 0, 0
        while idx1 < m and idx2 < n:
            if tmp[idx1] < nums2[idx2]:
                nums1[idx1+idx2] = tmp[idx1]
                idx1 += 1
            else:
                nums1[idx1+idx2] = nums2[idx2]
                idx2 += 1
        
        while idx1 < m:
            nums1[idx1+idx2] = tmp[idx1]
            idx1 += 1
        
        while idx2 < n:
            nums1[idx1+idx2] = nums2[idx2]
            idx2 += 1
        
        return