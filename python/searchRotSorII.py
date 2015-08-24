# Locating the pivot by binary search is impossible. Have to traverse the whole array.
# Takse O(n)

# CASES: 1111115, 1151111, 3344455, 3444553
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {boolean}
    def search(self, nums, target):
        if not nums: return

        