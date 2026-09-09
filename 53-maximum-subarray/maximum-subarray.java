class Solution {
    public int maxSubArray(int[] nums) {
        int cur_sum=0;
        int max_sum=Integer.MIN_VALUE;
        for(int i=0;i<nums.length;i++)
        {
            cur_sum=Math.max(nums[i],cur_sum+nums[i]);
            max_sum=Math.max(cur_sum,max_sum);
        }
        return max_sum;
        
    }
}