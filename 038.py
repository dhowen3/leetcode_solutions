class Solution:
    def get_next_cas(self, current):
        # split current into parts w/ cocunt of digit then digit
        parts = []
        n = len(current)
        i = 0
        while i < n:
            current_char = current[i]
            count = 1
            while i + 1 < n and current[i+1] == current_char:
                count += 1
                i += 1
            else:
                i += 1
            parts.append((count, current_char))


        next = ""
        for part in parts:
            next += str(part[0]) + str(part[1])
        return next

        # combine all those into str
        # return str
    def countAndSay(self, n: int) -> str:
        i = 1
        current = "1"
        for i in range(2,n+1):
            current = self.get_next_cas(current) # cas - short for "count and say"
            print("i", i)
            print("current", current)

        return current
