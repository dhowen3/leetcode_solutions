class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        power = 1
        current = 0
        for char in columnTitle[::-1]:
            current += power * (ord(char) - ord('A') + 1)
            power *= 26
        return current
