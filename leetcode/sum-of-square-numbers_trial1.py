from math import isqrt
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        j = int(isqrt(c))

        while i<=j:
            s = i*i + j*j
            if s == c:
                return True 
            elif s > c:
                j-=1
            else :
                i+=1
        return False 



        