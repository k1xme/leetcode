# This problem is essentially Cycle Detection problem.

class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {boolean}
    def canFinish(self, numCourses, prerequisites):
        if numCourses == 0: return False
        
        adjList = [[] for i in range(numCourses)]
        visited = [False]*numCourses
        
        # Construct adj list. Takes O(e)
        for e in prerequisites:
            adjList[e[1]].append(e[0])

        # DFS
        for i in range(numCourses ):
            if visited[i]: continue

            path = [(0, False) for j in range(numCourses)]
            stack = [(0, i)]
            
            while stack:
                depth, v = stack.pop()
                path[v] = (depth, True)

                for e in adjList[v]:
                    if path[e][1] and path[e][0] <= depth: return False
                    stack.append((depth+1, e))
                
                visited[v] = True

        return True
            

s = Solution()
print s.canFinish(3, [[1,0],[2,0],[0,1]])