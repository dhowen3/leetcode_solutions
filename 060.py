from math import factorial

class Solution:
    def get_perm_helper(self, n, k, current_str):
        # base case
        if n == 1:
            return [1]
        # recursive case
        n_minus_one_fact = factorial(n-1)
        digit = (k // n_minus_one_fact)
        new_k = k - digit * n_minus_one_fact
        following = self.get_perm_helper(n - 1, new_k, [])
        following = [each_dig + 1 if each_dig > digit else each_dig for each_dig in following]
        return [digit + 1] + following

    def getPermutation(self, n: int, k: int) -> str:
        k -= 1
        fn_list = self.get_perm_helper(n, k, [])
        return_str = ""
        for digit in fn_list:
            return_str += str(digit)
        return return_str
