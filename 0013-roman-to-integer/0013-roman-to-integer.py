class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        Roman_Numerals = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        l=[]
        for i in s:
            for x in Roman_Numerals:
                if i==x:
                 l.append(Roman_Numerals[x])
        score = 0 
        for i in range(0,len(l)-1):
            if l[i] < l[i+1]:
                score-=l[i]
            elif l[i]>=l[i+1]:
                score+=l[i]

        score = score + l[-1]
        return(score)

        [1000, 100, 1000, 10, 100, 1, 5]
                