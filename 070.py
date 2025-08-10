class Solution:
  def climbStairs(self, n: int) -> int:
    dp = []
    two_prior = 0
    one_prior = 1
    for i in range(n):
      new = one_prior + two_prior
      two_prior = one_prior
      one_prior = new
    return one_prior
