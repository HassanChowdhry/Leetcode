// https://leetcode.com/problems/unique-number-of-occurrences

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        hm = {}
        st = set()

        for num in arr:
            if num in hm:
                hm[num] += 1
            else:
                hm[num] = 1
        
        for num, value in hm.items():
            if value in st:
                return False
            st.add(value)

        return True
        