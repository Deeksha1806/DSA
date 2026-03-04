class Solution {
    public int searchInsert(int[] nums, int target) {
        int n=nums.length;
        if(nums[n-1]<target)
            return nums.length;
        else if(nums[n-1]==target)
            return n-1;
        for(int i=0;i<nums.length-1;i++)
        {
            if(nums[i]==target)
            return i;
            else if(nums[i]<target && nums[i+1]>target)
            return i+1;
            
        }
        return 0;
    }
}