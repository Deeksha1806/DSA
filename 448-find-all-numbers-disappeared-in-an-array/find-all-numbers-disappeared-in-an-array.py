class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        set_nums=set(nums)
        missed=[]
        n=len(nums)
        for i in range(1,n+1):
            if i not in set_nums:
                missed.append(i)
        return missed

        