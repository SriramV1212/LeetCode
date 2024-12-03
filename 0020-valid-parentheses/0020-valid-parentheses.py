class Solution:
    def isValid(self, s: str) -> bool:
        a=["(","{","["]
        b=[")","}","]"]
        p=0
        q=0
        r=0
        l=[]
        count=0
        if (len(s)%2)!=0 or s[0] in b:
            return(False)
        for i in range(len(s)):
            count+=1
            if s[i]==a[0]:
                p+=1
                l.append(s[i])
            if s[i]==a[1]:
                q+=1
                l.append(s[i])
            if s[i]==a[2]:
                r+=1
                l.append(s[i])
            if s[i]==b[0] and p==0:
                break
            if s[i]==b[1] and q==0:
                break
            if s[i]==b[2] and r==0:
                break
            if s[i]==b[0] and p>0:
                if l[len(l)-1]==a[0]:
                    p-=1
                    l.pop()
            if s[i]==b[1] and q>0:
                if l[len(l)-1]==a[1]:
                    q-=1
                    l.pop()
            if s[i]==b[2] and r>0:
                if l[len(l)-1]==a[2]:
                    r-=1
                    l.pop()
        if p==0 and q==0 and r==0 and count==len(s):
            return(True)
        else:
            return(False)
                
        


        