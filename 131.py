import itertools

'''
notes on dp:
b | oo | b
check if inner is palindrome, then check if first and last match
'''


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[False for j in range(n+1)] for i in range(n)]
        for k in range(1,n+1): # length of palindrome to target
            for i in range(n-k+1): # i denotes starting index
                if ((k == 1) or # one letter
                    (k == 2 and s[i] == s[i+1]) or # two letters
                    (s[i] == s[i + k - 1] and dp[i+1][i+k-1])): # three or more letters
                    dp[i][i+k] = True
        '''
        for row in dp:
            print(row)
        '''
        # dp[i][j] holds info if s[i:j] is a palindrome. now want to list all splits, checking if they're a palindrome
        if s == 1: return [s[0]]
        # illustrate the below - if n = 3, then inner_powerset holds (),(1),(2),(1,2) # at next line
        inner_powerset = chain.from_iterable(combinations([i+1 for i in range(n-1)],r) for r in range(n))
        to_return = []
        for poset in inner_powerset:
            # illustrate the below - if n = 3, then inner_powerset holds (0,3),(0,1,3),(0,2,3),(0,1,2,3) # at next line
            poset = [0] + [elt for elt in poset] + [n] #
            is_valid = True
            to_append = []
            for i in range(len(poset)-1):
                if not dp[poset[i]][poset[i+1]]:
                    print(s[poset[i]:poset[i+1]])
                    is_valid = False
                    break
                else:
                    to_append.append(s[poset[i]:poset[i+1]])
            if is_valid:
                to_return.append(to_append)
        return to_return
