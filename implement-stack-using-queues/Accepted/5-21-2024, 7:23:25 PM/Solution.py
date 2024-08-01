// https://leetcode.com/problems/implement-stack-using-queues

class MyStack:

    def __init__(self):
        self.n = 0
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.n += 1

    def pop(self) -> int:
        self.n -= 1
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return self.n==0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()