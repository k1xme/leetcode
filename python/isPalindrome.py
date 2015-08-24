# Using 2 pointers, one pointing to front and the other to the rear of the sring.

class Solution:
    # @param {string} s
    # @return {boolean}
    def isPalindrome(self, s):
        if not s:
            return True
        
        length = len(s)

        front = 0
        rear = len(s) - 1
        
        while front < rear:
            while front < rear and not s[front].isalnum():
                front += 1

            while front < rear and not s[rear].isalnum():
                rear -=1

            if s[front].lower() == s[rear].lower():
                front += 1
                rear -= 1
            else:
                return False
            
        return True

s = Solution()
p = '    '

print s.isPalindrome(p)