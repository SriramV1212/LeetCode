class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l=[]
        s=""
        c=""
        j=0
        for i in range(len(haystack)):
            if haystack[i]==needle[0]:
                l.append(i)
        
        for x in l:
            c=haystack[x:]
            for i in range(len(needle)):
                if i<len(c) and needle[j]==c[i] and ((s=="")or needle.startswith(s)):
                  s+=c[i]
                  j+=1
                else:
                  s=""
                  j=0
                  break
            if s==needle:
              break
        if s!=needle:
            return(-1)
        else:
            return(x)
        