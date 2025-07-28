class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(0,len(nums)-1):
            if(nums[i]==nums[i+1]):
                nums[i]=nums[i]*2
                nums[i+1]=0
        count=0
        j=0
        while j<len(nums):
            if(nums[j]==0):
                count=count+1
                nums.pop(j)
            else:
                j=j+1
        for k in range(0,count):
            nums.append(0)
        return nums