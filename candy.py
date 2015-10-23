class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if not ratings: return 0
        
        candy = [0] * len(ratings)
        
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candy[i] = candy[i-1]+1
                
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                if candy[i] <= candy[i+1]:
                    candy[i] = candy[i+1] + 1
        
        return sum(candy) + len(ratings)
                
sol = Solution()
print sol.candy([4,2,3,4,1])