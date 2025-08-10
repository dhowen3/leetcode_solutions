class Solution:
    def __init__(self):
        self.board = [[]]
        self.word = ""
        self.m, self.n = 0, 0
    
    def get_next(self, row, col):
        to_return = set()
        if row + 1 < self.m: to_return.add((row + 1, col))
        if row - 1 >= 0: to_return.add((row - 1, col))
        if col + 1 < self.n: to_return.add((row, col + 1))
        if col - 1 >= 0: to_return.add((row, col - 1))
        return to_return

    def search(self, row, col, index, visited):
        # base case 1:
        if index == len(self.word) - 1 and self.word[index] == self.board[row][col]:
            return True
        # base case 2:
        if self.word[index] != self.board[row][col]:
            return False
        # recursive case
        to_return = False
        visited.add((row,col))
        for next_cell in self.get_next(row, col) - visited:
            if self.search(next_cell[0], next_cell[1], index + 1,
                    visited.copy()):
                to_return = True
                break
        return to_return

    def exist(self, board: List[List[str]], word: str) -> bool:
        for row in board:
            print(row)
        self.board = board
        self.word = word

        self.m, self.n = len(board), len(board[0])
        match_found = False
        for i in range(self.m):
            for j in range(self.n):
                match_found = self.search(i,j, 0, set())
                if match_found: break
            if match_found: break
        return match_found
        
