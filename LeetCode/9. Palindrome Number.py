class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        
        x = str(x)
        length = len(x)
        
        for i in range(length//2):
            if x[i] != x[-(i+1)]:
                return False
            
        return True
        
        