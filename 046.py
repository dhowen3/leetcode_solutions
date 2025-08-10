class Solution:
    def permute_helper(self, left, right, to_return):
        n = len(left)
        if n == 0:
            to_return.append(right)
            return
        for i in range(n):
            self.permute_helper(left[0:i] + left[i+1:n], right + [left[i]], to_return)

    def permute(self, nums: List[int]) -> List[List[int]]:
        to_return = []
        self.permute_helper(nums, [], to_return)
        return to_return
