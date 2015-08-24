class Solution:
    """
    @param A: A positive integer which has N digits, A is a string.
    @param k: Remove k digits.
    @return: A string
    """
    def DeleteDigits(self, A, k):
        n = len(A)
        digit_num = n-k
        result = ""
        start = 0
        end = n - digit_num+1
        
        while digit_num > 0:
            i = start
            digit = int(A[start])
            for j in xrange(start, end):
                cur_digit = int(A[j])
                if cur_digit < digit:
                    digit = cur_digit
                    i = j
            
            result += A[i]
            digit_num -= 1
            start = i+1
            end = n - digit_num+1
        
        return str(int(result))

s = Solution()
print s.DeleteDigits("90249", 2)