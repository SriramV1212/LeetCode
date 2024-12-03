class Solution:
    def climbStairs(self, n: int) -> int:
        p=1
        c=1
        for i in range(n-1):
            t=c
            c=p+c
            p=t
        return c

        