class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[1]]
        for i in range(1,numRows):
            prev_row = pascal[-1]
            print(prev_row)
            current = []
            current.append(1)
            for j in range(len(prev_row) - 1):
                current.append(prev_row[j] + prev_row[j+1])
            current.append(1)
            pascal.append(current)
        return pascal

        
