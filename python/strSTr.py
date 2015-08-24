# KMP
# The key is to construct the table, which is the index for neeelde to backtrack.
# (find the proper suffix of substring that is equal to the prefix of the substring.)

class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
        if not haystack or not needle:
            return -1
            
        T = self.fillTable(needle)
        
        n_pos = 0
        needle_len = len(needle)
        hs_len = len(haystack)

        for pos in range(hs_len):
            while haystack[pos] != needle[n_pos] and n_pos > 0:
                n_pos = T[n_pos]

            if haystack[pos] == needle[n_pos]: n_pos += 1
            if n_pos == needle_len: return pos - needle_len + 1

        
        return -1
    
    # @return {integer[]} table
    def fillTable(self, needle):
        T = [0] * len(needle)
        T[0] = -1 # there is no LPS before the first char, so we define it as -1.
        
        lps = 0
        
        for i in range(1, len(needle)):
            # Keep backtrack until we find the last match position of the LPS
            # or we back to the head of the pattern string, which means we
            # there is no LPS before i.
            if i == 1:
                T[i] = 0
                continue

            while lps > 0 and needle[lps] != needle[i-1]:
                lps = T[lps]

            # If the last char of suffix match the last char of prefix,
            # we increase the length of LPS by 1 and fill it in the T[i]
            if needle[i-1] == needle[lps]:
                lps += 1
                T[i] = lps

        return T

s = Solution()


def computeFailArray(needle):
    fail = [0] * len(needle)
    fail[0] = -1
    
    for i in range(1, len(needle)):
        if needle[i-1] != needle[fail[i-1]]: fail[i] = 0
        else: fail[i] = fail[i-1] + 1
    
    return fail

print computeFailArray('issip')
        