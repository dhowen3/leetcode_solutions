from collections import deque

class Solution:
    def get_opening(self,char):
        to_return = ' '
        if char == ')':
            to_return = '('
        elif char == ']':
            to_return = '['
        elif char == '}':
            to_return = '{'
        else:
            raise Exception("unexpected char passed to get_opening(): ", char)
        return to_return

    def isValid(self, s: str) -> bool:
        q = deque()
        n = len(s)
        to_return = True
        for i in range(n):
            c = s[i]
            if c in ('(','[','{'):
                q.appendleft(c)
            elif c in (')',']','}') and len(q) > 0 and q[0] == self.get_opening(c):
                q.popleft()
            else:
                to_return = False
                break
        to_return = to_return and len(q) == 0
        return to_return
