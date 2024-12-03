class Solution:
    def climbStairs(self, n: int) -> int:
        def fact(m):
          c=1
          for i in range(1,m+1):
              c*=i
          return(c)
        ways=0
        for i in range(n+1):
             for j in range(n+1):
                 if (2*i + 1*j)==n:
                      k=fact(i+j)//(fact(i) * fact(j))
                      ways+=k
        return(ways)

        


        