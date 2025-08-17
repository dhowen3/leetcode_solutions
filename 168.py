class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        to_return = ""
        while columnNumber > 0:
            columnNumber -= 1
            x = columnNumber % 26 
            to_return = chr(ord('A') + x) + to_return
            columnNumber //= 26
        return to_return
