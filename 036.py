class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        one_through_nine = {i:False for i in range(1,10)}
        for i in range(9):
            # check rows
            copy_dict = {i:False for i in range(1,10)}
            row = board[i]
            for val in row:
                if val == '.':
                    continue
                val = int(val)
                if copy_dict[val]: # if it's checked twice
                    return False
                copy_dict[val] = True
        # check columns
        for j in range(9):
            copy_dict_col = {i:False for i in range(1,10)}
            for i in range(9):
                val = board[i][j]
                if val == '.':
                    continue
                val = int(val)
                if copy_dict_col[val]: # if it's checked twice
                    print("columns",i,j)
                    return False
                copy_dict_col[val] = True
        # check boxes
        for box_row in range(3):
            for box_col in range(3):
                copy_dict = {i:False for i in range(1,10)}
                for k in range(9):
                    row_in_box = k // 3
                    col_in_box = k % 3
                    val = board[(3 * box_row) + row_in_box][(3 * box_col) + col_in_box]
                    if val == '.':
                        continue
                    val = int(val)
                    if copy_dict[val]:
                        return False
                    else:
                        copy_dict[val] = True
        return True
