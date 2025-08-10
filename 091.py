class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s) 
        if n == 0:
            return 1
        if s[0] == "0":
            return 0
        z = []
        for i in range(1,n):
            if s[i] == '0':
                if s[i-1] == '1' or s[i-1] == '2':
                    z.append(i)
                    z.append(i-1) # 0 must be closed
                else:
                    return 0
        z_prime = list(set(range(n)) - set(z))
        # no zeros for indices in z prime
        dp = [1 for i in range(len(z_prime) + 1)]
        for i in range(len(z_prime) - 1):
            dp_i = i + 1 # dp index - one more than i
            c =  s[z_prime[i]] # c - Current 
            x = s[z_prime[i+1]] # x - neXt
            if z_prime[i+1] != z_prime[i] + 1:
                dp[dp_i+1] = dp[dp_i]
            elif c == "1":
                dp[dp_i + 1] = dp[dp_i] + dp[dp_i - 1] # fibonacci
            elif c == "2" and x >= "0" and x <= "6":
                dp[dp_i + 1] = dp[dp_i] + dp[dp_i - 1] # fibonacci
            else:
                dp[dp_i + 1] = dp[dp_i]
        print(dp)
        return dp[-1]

