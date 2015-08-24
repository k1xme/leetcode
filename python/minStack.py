# Keep a field that record the min elem in stack.
# NEW: store tuple with the new element and the current min elemnt into the stack.
# Thus the retrival would all be constant time.

class MinStack:
    # @param x, an integer
    # @return an integer
    top_elem = None
    stack = []
    
    def push(self, x):
        if self.stack:
            min_elem = x if x < self.top_elem[1] else self.top_elem[1]
        else: min_elem = x
              
        
        self.stack.append((x, min_elem))
        self.top_elem = (x, min_elem)

    # @return nothing
    def pop(self):
        if not self.stack:
            return 
        # change the top_elem
        self.top_elem = self.stack.pop()
        self.stack.append(self.top_elem)
        

    # @return an integer
    def top(self):
        return self.top_elem[0]

    # @return an integer
    def getMin(self):
        return self.top_elem[1]

s = MinStack()

s.push(-1)

print s.top()
print s.getMin()