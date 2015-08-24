# Uses hashmap to store show-up numbers with the length of sequences they are in.

from collections import defaultdict

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def longestConsecutive(self, nums):
        if not nums: return 0
        
        longest = 0
        showed = defaultdict(lambda: 0)
        
        for n in nums:
            # Duplicates
            if showed[n] > 0: continue
            # Check if there are consecutive seqs next to n.
            leftSeq, rightSeq = showed[n-1], showed[n+1]
            newLongest = leftSeq+rightSeq+1
            showed[n] = newLongest
            # Update the longest seq
            longest = max(longest, newLongest)
            # Update the seq len of the head and tail in the dict.
            showed[n-leftSeq] = newLongest # Update head with the new seq len.
            showed[n+rightSeq] = newLongest
        
        return longest

s = Solution()
print s.longestConsecutive([4,0,-4,-2,2,5,2,0,-8,-8,-8,-8,-1,7,4,5,5,-4,6,6,-3])