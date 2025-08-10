class Solution:
    def grayCode(self, n: int) -> List[int]:
        to_return = [0,1]
        i = 1
        while i < n:
            new = []
            for el in to_return[::-1]:
                new.append(el | (1 << i))
            to_return += new
            i += 1
        return to_return
