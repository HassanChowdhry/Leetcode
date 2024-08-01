// https://leetcode.com/problems/running-sum-of-1d-array

class Solution 
{
    public int[] runningSum(int[] nums)
    {
         int Sum;
        int[] ArraySum = new int[nums.length];
       for(int i = 0; i < nums.length ; i++)
       {
            Sum = nums[i];
          for (int j = i ; j >= 0; j-- )
          {
              if (j > 0)
              {
                  Sum += nums[j - 1];
              }
               
          }
          ArraySum[i] = Sum;
       }

        return ArraySum;
    }
}