class Solution:
    def reverseWords(self, s: str) -> str:
        to_return = ""
        for word in s.strip()[::-1].split():
            to_return += word[::-1] + " "
        return to_return[:-1]
        
        
