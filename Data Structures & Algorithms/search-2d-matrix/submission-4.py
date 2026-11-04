class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rl, rr = 0, len(matrix) - 1
        cl, cr = 0, len(matrix[0]) - 1

        while rl <= rr:
            r_mid = rl + (rr - rl) // 2
            if matrix[r_mid][0] <= target <= matrix[r_mid][-1]:
                while cl <= cr:
                    c_mid = cl + (cr - cl) // 2
                    if target == matrix[r_mid][c_mid]:
                        return True
                    elif target > matrix[r_mid][c_mid]:
                        cl = c_mid + 1
                    else:
                        cr = c_mid - 1
                return False

            elif matrix[r_mid][0] > target:
                rr = r_mid - 1
            
            else:
                rl = r_mid + 1

        return False