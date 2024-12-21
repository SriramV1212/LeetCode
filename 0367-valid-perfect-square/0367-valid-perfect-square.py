class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        z= num**(1/2)
        h = int(z)
        if h==z:
            return(True)
        else:
            return(False)
        