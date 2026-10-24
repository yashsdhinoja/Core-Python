class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False

        num = x
        result = 0

        while num > 0:
            id = num % 10
            result = (result * 10) + id
            num = num // 10
            
        return x == result
   
        
print(Solution().isPalindrome(121))  # Returns True
print(Solution().isPalindrome(-121)) # Returns False
print(Solution().isPalindrome(10))   # Returns False