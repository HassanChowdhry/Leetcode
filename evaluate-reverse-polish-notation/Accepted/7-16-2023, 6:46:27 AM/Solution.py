// https://leetcode.com/problems/evaluate-reverse-polish-notation

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
              # declare
      stack = []
      
      # logic
      for token in tokens:
        if token == '*':
          stack.append(stack.pop() * stack.pop())
        elif token == '+':
          stack.append(stack.pop() + stack.pop())
        elif token == '/':
          num1, num2 = stack.pop(), stack.pop()
          stack.append(int(num2 / num1))
        elif token == '-':
          num1, num2 = stack.pop(), stack.pop()
          stack.append(num2 - num1)
        else:
          stack.append(int(token))
      
      # return res
      return stack[0]