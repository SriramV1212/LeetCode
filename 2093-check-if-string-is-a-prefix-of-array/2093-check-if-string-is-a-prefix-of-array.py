class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        a=""
        b=""
        for x in words:
            a+=x
            if s.startswith(a):
                b=a
                continue
            else:
                break
        if b==s:
            return(True)
        else:
            return(False)
        

        