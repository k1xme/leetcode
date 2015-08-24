# If sum(gas) < sum(cost), return -1.
# Otherwise, we start from index 0, skip those stations that cost[i] > gas[i].
# Calculate the gas remained in the tank if start from station i. 
# NOTE: have to break the cycle.


# Can I assume there is only one answer?
class Solution:
    # @param {integer[]} gas
    # @param {integer[]} cost
    # @return {integer}
    def canCompleteCircuit(self, gas, cost):
        if not gas or sum(gas) - sum(cost)<0: return -1
        
        n = len(gas)
        start = n - 1
        end = 0
        tank = gas[start] - cost[start]
        
        while end < start:
            print tank, start , end
            if tank >= 0:
                tank += gas[end] - cost[end]
                end += 1
            else:
                start -= 1
                tank += gas[start] - cost[start]
        
        return start

s = Solution()
gas = [1,2,3,3]
cost = [2,1,5,1]
gas1 = [1,2,3,4,5]
gas2 = [2,1,3]
cost1 = [3,4,5,1,2]
cost2 = [3,1,2]
print s.canCompleteCircuit(gas2,cost2)