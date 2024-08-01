// https://leetcode.com/problems/relative-sort-array

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        k = max(arr1)
        freq = Counter(arr1)
        res = []

        for num in arr2:
            for i in range(freq[num]):
                res.append(num)
            del freq[num]
        
        for num in range(k+1):
            if num not in freq: continue

            for i in range(freq[num]):
                res.append(num)
            del freq[num]
        
        return res