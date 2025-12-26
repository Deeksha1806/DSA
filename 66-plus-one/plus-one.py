class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        p=""
        for i in digits:
            p=p+str(i)
        k=int(p)+1
        g=list(str(k))
        h=list(map(int,g))
        return h
