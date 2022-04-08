class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 이진탐색 2번? => 만약 첫 번째 row가 [1, 3, 5, 7, 9]이고, target 13이 2번째 column에 있다면 찾지 못하는 문제가 발생한다. 
        # => 첫 번째 행의 모든 경우 탐색
            
        for i in range(len(matrix[0])):
            if matrix[0][i] > target:
                continue
            elif matrix[0][i] < target:
                if self.binary_search(matrix, target, i):
                    return True
            else:
                return True
        return False 
    
    def binary_search(self, matrix, target, row):
        col_start = 0
        col_end = len(matrix)-1

        while col_start <= col_end:

            mid = (col_start + col_end) // 2

            if matrix[mid][row] > target:
                col_end = mid -1

            elif matrix[mid][row] < target:
                col_start = mid + 1

            else:
                return True
        return False