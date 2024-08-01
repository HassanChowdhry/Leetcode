// https://leetcode.com/problems/fizz-buzz

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        fizz_buzz = []           
        for i in range(1, n + 1):
            is_divisible_by_3 = i % 3 == 0
            is_divisible_by_5 = i % 5 == 0
            if is_divisible_by_3 and is_divisible_by_5:
                fizz_buzz.append('FizzBuzz')
            elif is_divisible_by_5:
                fizz_buzz.append('Buzz')
            elif is_divisible_by_3:
                fizz_buzz.append('Fizz')
            else:
                fizz_buzz.append(f'{i}')             
        return fizz_buzz