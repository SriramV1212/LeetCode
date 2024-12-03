class Solution:
    def climbStairs(self, n: int) -> int:
        p=1
        c=1
        for i in range(1,n):
            t=c
            c=p+c
            p=t
        return c

        