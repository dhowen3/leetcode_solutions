class Solution:
    def __init__(self):
        self.matrix = [[]]
    
    """
    corners (check)
    middle (check)
    edges ()
    """

    def rotate_corners(self, x, y, n):
        temp = self.matrix[x+n-1][y]
        self.matrix[x+n-1][y] = self.matrix[x+n-1][y+n-1] # bottom left from bottom right
        self.matrix[x+n-1][y+n-1] = self.matrix[x][y+n-1] # bottom right from upper right
        self.matrix[x][y+n-1] = self.matrix[x][y] # upper right from upper left
        self.matrix[x][y] = temp # upper left from bottom left
    
    def rotate_edges(self, x,y,n):
        edge_length = n - 2
        for i in range(edge_length):
            '''
            # upper "edge" is defined from 1..n-2
            self.matrix[x][y+1+i] # upper edge
            self.matrix[x+1+i][y+n-1] # right edge
            self.matrix[x+n-1][y+n-i-1-1] # bottom edge
            self.matrix[x+n-i-1-1][y] # left edge
            '''
            temp = self.matrix[x][y+1+i]
            self.matrix[x][y+1+i] = self.matrix[x+n-i-1-1][y] # upper from left
            self.matrix[x+n-i-1-1][y] = self.matrix[x+n-1][y+n-i-1-1] # left from bottom 
            self.matrix[x+n-1][y+n-i-1-1] = self.matrix[x+1+i][y+n-1] # bottom from right
            self.matrix[x+1+i][y+n-1] = temp # right from upper

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.matrix = matrix
        n = len(matrix)
        end_index = 0
        if n % 2 == 0:
            end_index = int(n / 2)
        else:
            end_index = int((n - 1) / 2)
        x = 0
        y = 0
        for i in range(end_index):
            # rotate corners, rotate edges
            self.rotate_corners(x,y,n)
            self.rotate_edges(x,y,n)
            n -= 2
            x += 1
            y += 1
