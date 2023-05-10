class Solution:
    def arraySign(self, nums: List[int]) -> int:
            
            r = 1
            for _ in nums:
                r = r * _
                        
            if r > 0:
                return 1
            elif r < 0:
                return -1
            else:
                return 0