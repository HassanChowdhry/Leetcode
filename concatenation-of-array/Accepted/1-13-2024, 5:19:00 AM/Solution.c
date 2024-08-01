// https://leetcode.com/problems/concatenation-of-array

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getConcatenation(int* nums, int numsSize, int* returnSize) {
  int* doubled_nums = malloc(2 * numsSize * sizeof(int));
  for(int i = 0; i < numsSize; i++) {
    doubled_nums[i] = nums[i];
    doubled_nums[i + numsSize] = nums[i];
  }

  *returnSize = 2 * numsSize;
  return doubled_nums;
}