class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        u, d = 0, row - 1
        col = len(matrix[0])
        l, r = 0, col - 1

        final_row = -1


        while d >= u:
            mid = u + (d - u) // 2

            if target > matrix[mid][-1]:
                u = mid + 1
            elif target < matrix[mid][0]:
                d = mid - 1
            else:
                final_row = mid
                break

        if final_row == -1:
            return False

        while r >= l:
            mid = l + (r - l) // 2
            if target < matrix[final_row][mid]:
                r = mid - 1
            elif target > matrix[final_row][mid]:
                l = mid + 1
            else:
                return True

        return False
