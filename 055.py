class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        increasing, row_traversal = True, True
        row_start, row_end = 0, len(matrix)
        column_start, column_end = 0, len(matrix[0])
        to_return = []
        while row_end - row_start > 0 and column_end - column_start > 0:
            if increasing:
                if row_traversal:
                    i,j = row_start, column_start
                    for j in range(column_start,column_end):
                        to_return.append(matrix[i][j])
                    row_start += 1
                    increasing, row_traversal = True, False
                else: 
                    i,j = row_start, column_end - 1 
                    for i in range(row_start,row_end):
                        to_return.append(matrix[i][j])
                    column_end -= 1
                    increasing, row_traversal = False, True
            else: # decreasing 
                if row_traversal:
                    i,j = row_end - 1, column_end - 1 
                    for j in range(column_end - 1, column_start -1, -1):
                        to_return.append(matrix[i][j])
                    row_end -= 1
                    increasing, row_traversal = False, False
                else:
                    i,j = row_end - 1, column_start
                    for i in range(row_end - 1, row_start -1, -1):
                        to_return.append(matrix[i][j])
                    column_start += 1
                    increasing, row_traversal = True, True
        return to_return
