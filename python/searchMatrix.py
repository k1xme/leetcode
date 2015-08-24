class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def searchMatrix(self, matrix, target):
        if not matrix: return False

        flat = []
        
        for row in matrix:
            flat += row
        
        high, low = len(flat) - 1, 0
        
        while low <= high:
            mid = (high-low)/2 + low
            print mid
            if flat[mid] == target: return True
            if flat[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        
        return False

s = Solution()
a = [[1,1],[2,2]]
print s.searchMatrix([[1,3]], 3)