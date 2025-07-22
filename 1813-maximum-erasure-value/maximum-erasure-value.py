class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        l=0
        a=set()
        cur_sum=0
        max_sum=0
        for r in range(0,len(nums)):
            while(nums[r] in a):
                
                cur_sum-=nums[l]
                a.remove(nums[l])
                l+=1
            
            cur_sum+=nums[r]
            a.add(nums[r])
            max_sum=max(cur_sum,max_sum)
        return max_sum
