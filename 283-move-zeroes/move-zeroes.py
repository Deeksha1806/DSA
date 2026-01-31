class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        count=0
        i=0
        while(i<len(nums)):

            if(nums[i]==0):
                nums.pop(i)
                count=count+1
            else:
                i=i+1
        for i in range(0,count):         
            nums.append(0)
        return nums

       