// https://leetcode.com/problems/maximum-product-subarray

class Solution:
    def maxProduct(self, nums: List[int]) -> int:   
        min_num = nums[0]
        max_num = nums[0]
        res = [[min_num, max_num]]
        product = max_num

        for num in nums[1::]:
            min_num = min(num, num*res[-1][0], num*res[-1][1])
            max_num = max(num, num*res[-1][0], num*res[-1][1])
            res.append([min_num, max_num])

            product = max(product, max_num)
        
        print(res)
        return product