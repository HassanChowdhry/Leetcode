// https://leetcode.com/problems/count-numbers-with-unique-digits-ii

class Solution:
    def numberCount(self, a: int, b: int) -> int:
        #declare
        count = 0

        # main
        for i in range(a, b+1):
            if i < 10:
                count += 1
                continue
            
            num_set = set()
            is_unique = True
            for num in str(i):
                if num in num_set:
                    is_unique = False
                num_set.add(num)
            count += (1 if is_unique else 0)
        
        # end
        return count
