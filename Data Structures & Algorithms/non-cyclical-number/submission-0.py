class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        loop = True
        sum = 0
        while sum not in s:
            while n>0:
                digit = n%10
                n = n//10
                sum += digit**2
            if sum == 1:
                return True
            elif sum in s:
                return False
            s.add(sum)
            n = sum
            sum = 0
        return False

            
        