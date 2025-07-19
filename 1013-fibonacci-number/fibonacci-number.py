class Solution:
    def fib(self, n: int) -> int:
        if(n==0):
            return 0
        prev=0
        cur=1
        next=prev+cur
        for i in range(1,n):
            prev=cur
            cur=next
            next=prev+cur
        return cur