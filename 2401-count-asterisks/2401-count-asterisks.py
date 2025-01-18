class Solution(object):
    def countAsterisks(self, s):
        count=0
        flag=0
        for x in s:
            if x=="|":
                flag+=1
            if x=="*" and flag%2==0:
                count+=1
        return(count)
        
        