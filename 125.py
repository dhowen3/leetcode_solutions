class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        # convert string to letters only
        s_length : int = len(s)
        i : int = 0
        while i < s_length:
            num_or_letter : bool = s[i].isalpha() or s[i].isdigit()
            if not num_or_letter:
                s = s[:i] + s[i+1:]
                s_length -= 1
            else:
                i = i + 1
        half_length : int = int(len(s)/2)
        print(s)
        for i in range(half_length):
            from_front : chr = s[i]
            from_back : chr = s[-1 - i]
            if from_front != from_back:
                return False
        return True
        
