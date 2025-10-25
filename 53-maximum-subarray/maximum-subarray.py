class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum=0
        max_sum=float("-inf")
        for i in range(0,len(nums)):
            cur_sum=max(nums[i],nums[i]+cur_sum)
            max_sum=max(cur_sum,max_sum)
        return max_sum
        