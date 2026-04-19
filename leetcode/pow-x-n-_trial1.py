class Solution:
    def myPow(self, x: float, n: int) -> float:        
        def pw(n):
            if n == 0 :
                return 1

            half = pw(n//2)

            if n % 2 == 0:
                return half * half
            else :
                return half * half * x
      
        if n<0:
            return 1/pw(-n)

        return pw(n)