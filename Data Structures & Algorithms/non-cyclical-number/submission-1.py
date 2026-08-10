class Solution:
    def isHappy(self, n: int) -> bool:
        def sumOfSquares(n):
            out = 0
            while n>0:
                digit = n%10
                n = n//10
                out += digit**2
            return out
            
        s = set()
        while n not in s:
            s.add(n)
            n = sumOfSquares(n)
            if n == 1:
                return True
        return False

        