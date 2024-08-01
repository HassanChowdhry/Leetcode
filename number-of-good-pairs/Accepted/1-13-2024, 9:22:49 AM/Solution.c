// https://leetcode.com/problems/number-of-good-pairs

int numIdenticalPairs(int* nums, int numsSize) {
    int res = 0;

    for (int i = 0; i < numsSize; ++i) {
        for (int j = i+1; j < numsSize; ++j) {
            if (nums[i] == nums[j]) {
                res++;
            }
        }
    }

    return res;
}