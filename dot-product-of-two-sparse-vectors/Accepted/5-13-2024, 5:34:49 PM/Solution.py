// https://leetcode.com/problems/dot-product-of-two-sparse-vectors

class SparseVector:
    def __init__(self, nums: List[int]):
        self.cord = nums

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        nums1 = self.cord
        nums2 = vec.cord
        res = 0

        for i in range(len(nums1)):
            res += (nums1[i]*nums2[i])
        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)