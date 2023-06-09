#Exercicio muito divertido, me ensinou busca binária.
#Além de revelar que busca binária n necessariamente envolve um vetor

class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x < 2:
            return x
        
        left, right = 0, x
        
        while left < right:
            
            mid = (left + right) // 2
            
            if mid * mid <= x < (mid + 1) * (mid + 1):
                return mid
            
            elif x < mid * mid:
                right = mid
                
            else:
                left = mid + 1
                
        return left
