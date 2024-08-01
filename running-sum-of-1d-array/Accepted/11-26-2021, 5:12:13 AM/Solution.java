// https://leetcode.com/problems/running-sum-of-1d-array

class Solution 
{
    public int[] runningSum(int[] nums)
    {
          int[] ArraySum = new int[nums.length];
       ArraySum[0] = nums[0];
       for (int i = 1; i < nums.length; i++)
       {
           ArraySum[i] = ArraySum[i-1] + nums[i];
       }
       return ArraySum;
    }
}