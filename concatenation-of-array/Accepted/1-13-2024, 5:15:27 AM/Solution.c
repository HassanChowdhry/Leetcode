// https://leetcode.com/problems/concatenation-of-array

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getConcatenation(int* nums, int numsSize, int* returnSize) {
    int * res = (int*) malloc(numsSize*2 * sizeof(int));

    for (int i = 0; i <= 1; ++i) {
        for (int j = 0; j < numsSize*2; ++j) {
            res[j] = nums[j%numsSize];
        }
    }

    *returnSize = numsSize*2;
    return res;
}