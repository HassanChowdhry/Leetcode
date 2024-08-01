// https://leetcode.com/problems/sum-of-two-integers

class Solution {
public:
    int getSum(int a, int b) {
        int carry = a & b;
        int xor_result = a ^ b;

        while (carry != 0) {
            carry <<= 1;
            int nxt_carry = carry & xor_result;
            xor_result = xor_result ^ carry;
            carry = nxt_carry;
        }

        return xor_result;
    }
};