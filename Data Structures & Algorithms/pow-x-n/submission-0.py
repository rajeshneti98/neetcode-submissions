class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif x == 0:
            return 0
        elif n>0:
            pro = self.myPow(x, n//2)
            if n%2==0:
                return pro*pro
            else:
                return x*pro*pro
        else:
            return 1.0/(self.myPow(x,-n))
        