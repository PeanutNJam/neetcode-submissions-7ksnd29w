class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1
        
        l, r = 0, len(nums1)
        
        while True:  # Guaranteed to find answer
            i = l + (r - l) // 2
            j = (total + 1) // 2 - i
            
            A_left = nums1[i - 1] if i > 0 else float("-inf")
            A_right = nums1[i] if i < len(nums1) else float("inf")
            B_left = nums2[j - 1] if j > 0 else float("-inf")
            B_right = nums2[j] if j < len(nums2) else float("inf")
            
            if A_left <= B_right and B_left <= A_right:
                if total % 2 == 1:
                    return max(A_left, B_left)
                else:
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2
            elif A_left > B_right:
                r = i - 1
            else:
                l = i + 1
