class Solution(object):
    def myPowHelper(self, x, n):
    # base cases
        if n == 0:
            return 1
        if n == 1:
            return x
        # recursive case
        if n % 2 == 0:
            half = self.myPowHelper(x, n / 2)
            return half * half
        else:
            half_of_minus_one = self.myPowHelper(x, (n-1)/ 2)
            return x * half_of_minus_one * half_of_minus_one

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if x == 0:
            return 0
        if n < 0:
            return 1 / (self.myPowHelper(x,-n))
        return self.myPowHelper(x,n)
        
        
        
