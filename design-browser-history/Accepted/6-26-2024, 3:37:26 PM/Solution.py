// https://leetcode.com/problems/design-browser-history

class BrowserHistory:

    def __init__(self, homepage: str):
        self.back_stack = [homepage]
        self.forward_stack = []        

    def visit(self, url: str) -> None:
        self.back_stack.append(url)
        self.forward_stack = []        
        
    def back(self, steps: int) -> str:
        while len(self.back_stack) > 1 and steps != 0:
            self.forward_stack.append(self.back_stack.pop())
            steps -= 1
        return self.back_stack[-1]
        

    def forward(self, steps: int) -> str:
        while len(self.forward_stack) > 0 and steps != 0:
            self.back_stack.append(self.forward_stack.pop())
            steps -= 1
        return self.back_stack[-1]
        