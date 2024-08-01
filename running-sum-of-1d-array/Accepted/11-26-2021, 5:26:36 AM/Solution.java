// https://leetcode.com/problems/running-sum-of-1d-array

class Solution 
{
    public int[] runningSum(int[] nums)
    {
        int sum;
        int[] arraySum = new int[nums.length];
        for(int i = 0; i < nums.length; i++)
        {
            sum = nums[i];
            for (int j = i; j >= 0; j-- )
            {
                if (j > 0)
                {
                    sum += nums[j - 1];
                }
            }
            arraySum[i] = sum;
        }

        return arraySum;
    }
}