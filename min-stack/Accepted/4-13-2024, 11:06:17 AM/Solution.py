// https://leetcode.com/problems/min-stack

class MinStack:

    # have a min with each push untill you push a num less than that even
    # you might pop 
    def __init__(self):
        self.stack =[]
        self.min = float("inf")
        self.len = 0

    def push(self, val: int) -> None:
        self.min = min(val, self.min)
        self.stack.append((val, self.min))
        self.len += 1

    def pop(self) -> None:
        self.stack.pop()[0]
        self.len -= 1
        if self.len < 1:
            self.min = float("inf")
        else: 
            self.min = self.stack[self.len-1][1]

    def top(self) -> int:
        return self.stack[self.len-1][0]
        

    def getMin(self) -> int:
        return self.stack[self.len-1][1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()