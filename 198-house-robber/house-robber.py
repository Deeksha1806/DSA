class Solution:
    def rob(self, nums: List[int]) -> int:
        h1=0
        h2=0
        for i in nums:
            cur=max(h1,h2+i)
            h2=h1
            h1=cur
        return h1