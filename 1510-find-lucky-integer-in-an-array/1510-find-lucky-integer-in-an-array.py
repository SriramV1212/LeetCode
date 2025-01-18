class Solution:
    def findLucky(self, arr: List[int]) -> int:
        d={}
        l=[]
        for x in arr:
            if x not in l:
                d.update({x:1})
                l.append(x)
            else:
                y=d.get(x)
                y+=1
                d.update({x:y})
        lucky=[]
        for x,y in d.items():
            if x==y:
                lucky.append(y)
        if lucky==[]:
            return(-1)
        else:
            return(max(lucky))

        



               
        