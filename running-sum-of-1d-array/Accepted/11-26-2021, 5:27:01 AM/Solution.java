// https://leetcode.com/problems/running-sum-of-1d-array

class Solution 
{
    public int[] runningSum(int[] nums)
    {
        int[] arraySum = new int[nums.length];
        arraySum[0] = nums[0];
        for (int i = 1; i < nums.length; i++)
        {
            arraySum[i] = arraySum[i-1] + nums[i];
        }
        return arraySum;
    }
}