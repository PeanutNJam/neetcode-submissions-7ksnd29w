class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = left_max = right_max = 0
        

        while r > l:
            left_max = max(left_max, height[l])
            right_max = max(right_max, height[r])

            if left_max < right_max:
                res += left_max - height[l]
                l += 1
            
            else: 
                res += right_max - height[r]
                r -= 1

        return res