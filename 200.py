class UnionNode:
    def __init__(self):
        self.parent = None
        self.children = []

class UnionFind:
    def __init__(self):
        self.sets = []

    def find(self, current_node : UnionNode) -> UnionNode:
        current = current_node
        current_parent = current_node.parent
        while current_parent is not None:
            current = current_parent
            current_parent = current.parent
        return current


    
    def union(self, node1 : UnionNode, node2 : UnionNode):
        parent1 = self.find(node1)
        parent2 = self.find(node2)
        if parent1 == parent2:
            return
        else:
            parent1.children.append(parent2)
            parent2.parent = parent1
            self.sets.remove(parent2)

    def add_set(self, node):
        self.sets.append(node)
  
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        num_islands = 0
        union_find = UnionFind()
        # process cell at index 0,0
        if grid[0][0] == '1':
            new_node = UnionNode()
            union_find.add_set(new_node)
            grid[0][0] = new_node
        # process first row, all columns
        for j in range(1,n):
            if grid[0][j] == '1':
                new_node = UnionNode()
                union_find.add_set(new_node)
                grid[0][j]= new_node
                if grid[0][j-1] != '0':
                    union_find.union(grid[0][j-1], new_node)
        # process first column, all rows
        for i in range(1,m):
            if grid[i][0] == '1':
                new_node = UnionNode()
                union_find.add_set(new_node)
                grid[i][0]= new_node
                if grid[i - 1][0] != '0':
                    union_find.union(grid[i-1][0], new_node)
        # now process all subseq. rows, cols, top left to lower right, 
        # checking above and left of each current node
        for i in range(1,m):
            for j in range(1,n):
                if grid[i][j] == '1':
                    new_node = UnionNode()
                    union_find.add_set(new_node)
                    grid[i][j] = new_node
                    if grid[i - 1][j] != '0':
                        union_find.union(grid[i-1][j], new_node)
                    if grid[i][j - 1] != '0':
                        union_find.union(grid[i][j-1], new_node)
        return len(union_find.sets) 
