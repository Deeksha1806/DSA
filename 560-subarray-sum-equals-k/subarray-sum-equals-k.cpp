class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int count=0,sum=0,i;
        for(i=0;i<nums.size();i++)
        {
            sum=nums[i];
            if(sum==k)
            count=count+1;
        
        for(int j=i+1;j<nums.size();j++)
        {
            sum=sum+nums[j];
            if(sum==k)
            count=count+1;
        }
        }
        return count;
    }
};