class Solution:
    # @param {integer} numCourses
    # @param {integer[][]} prerequisites
    # @return {integer[]}
    def findOrder(self, numCourses, prerequisites):
        if not prerequisites:
            return [i for i in range(0, numCourses)]
        if numCourses == 0: return []
        
        adjList = [[] for i in range(numCourses)]
        #rootCourses = [True]*numCourses
        needCourses = [[] for i in range(numCourses)]
        
        for pre in prerequisites:
            adjList[pre[1]].append(pre[0])
            needCourses[pre[0]].append(pre[1])
         #   rootCourses[pre[0]] = False
            
        # Do topology sort by DFS here.
        visited = [False]*numCourses
        path = []
        
        for i in range(numCourses):
            if needCourses[i] or visited[i]: continue
            stack = [i]
            while stack:
                v = stack.pop()
                for c in adjList[v]:
                    needCourses[c].remove(v)
                    if not needCourses[c]: stack.append(c)
                path.append(v)
                visited[v] = True
        
        return path if len(path) == numCourses else []

s = Solution()
print s.findOrder(4, [[0,1],[3,1],[1,3],[3,2]])