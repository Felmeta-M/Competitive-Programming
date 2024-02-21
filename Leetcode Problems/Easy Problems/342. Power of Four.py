class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        while n>0:
            if n==1:
                return True
            elif n%4==0:
                n/=4
            else:
                return False
        