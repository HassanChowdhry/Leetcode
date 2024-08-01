// https://leetcode.com/problems/fizz-buzz

class Solution:
    def helper(self, n, counter, fizz_buzz):
        if n <  counter: return ''
        is_divisible_by_3 = counter % 3 == 0
        is_divisible_by_5 = counter % 5 == 0
        if is_divisible_by_3 and is_divisible_by_5:
            fizz_buzz.append('FizzBuzz')
        elif is_divisible_by_5:
            fizz_buzz.append('Buzz')
        elif is_divisible_by_3:
            fizz_buzz.append('Fizz')
        else:
            fizz_buzz.append(f'{counter}')
        self.helper(n, counter + 1, fizz_buzz)
        return fizz_buzz
            
    def fizzBuzz(self, n: int) -> List[str]:
        return self.helper(n, 1, []) 