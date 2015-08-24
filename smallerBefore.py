class SegTreeNode:
    
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.count = 0
        self.left = self.right = None

    def __repr__(self):
        return "(" + str(self.start) + ", " + str(self.end) + ", " + str(self.count) + ")"


# The insertion of segment tree!
class Solution:
    """
    @param A: A list of integer
    @return: Count the number of element before this element 'ai' is 
             smaller than it and return count number list
    """
    segTree = None
    def countOfSmallerNumberII(self, A):
        if not A: return []
        self.buildTree()
        
        result = []
        count = 0
        for num in A:
            count += 1
            print count, num
            result.append(self.query(self.segTree, num))

        return result        
        
    def buildTree(self):
        if self.segTree: return
    
        def build(start, end):
            if start == end: return SegTreeNode(start, end)
            
            r = SegTreeNode(start, end)
            r.left = build(start, (start+end)/2)
            r.right = build((start+end)/2+1, end)
            
            return r
        
        self.segTree = build(0, 10000)
    

    # Increment the count after query along the path.
    def query(self, root, num):
        root.count += 1
        if root.start == root.end: return 0
        if num == root.end:
            right = self.query(root.right, num)
            return root.left.count + right
        
        left_end = (root.start + root.end)/2
        right_start = (root.start + root.end)/2+1
        
        if num <= left_end: return self.query(root.left, num)
        
        return root.left.count + self.query(root.right, num)                        
            
        
s = Solution()
print s.countOfSmallerNumberII([26,78,27,100,33,67,90,23,66,5,38,7,35,23,52,22,83,51,98,69,81,32,78,28,94,13,2,97,3,76,99,51,9,21,84,66,65,36,100,41])