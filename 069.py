class Solution:
    ''' strategy : iterative binary search '''
    def my_sqrt_helper(self, x, lower_bound, upper_bound):
        while upper_bound - lower_bound > 1:
            guess = int(lower_bound + (upper_bound - lower_bound) / 2)
            if guess * guess > x:
                upper_bound = guess
            else:
                lower_bound = guess
        return lower_bound
        


    def mySqrt(self, x: int) -> int:
        retval = 0
        if x == 0:
            retval = 0
        elif x == 1:
            retval = 1
        else: 
            retval = self.my_sqrt_helper(x,1,x)
        return retval
