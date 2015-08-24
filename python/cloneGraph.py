# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node: return node
        
        nodes = {}
        
        stack = []
        
        root_label = node.label
        
        stack.append(node)
        
        while stack:
            new_v = None
            v = stack.pop()
            if v.label not in nodes:
                new_v = UndirectedGraphNode(v.label)
                nodes[v.label] = new_v
            else: continue
            
            # connect with neighbors.
            for neighbor in v.neighbors:
                if neighbor.label not in nodes:
                    new_nb = UndirectedGraphNode(neighbor.label)
                else: new_nb = nodes[neighbor.label]
                new_v.neighbors.append(new_nb)
                if neighbor is not v: stack.append(neighbor)
        
        return nodes[root_label]

s = Solution()
root = UndirectedGraphNode(0)
root.neighbors.append(root)
root.neighbors.append(root)
print s.cloneGraph(root)