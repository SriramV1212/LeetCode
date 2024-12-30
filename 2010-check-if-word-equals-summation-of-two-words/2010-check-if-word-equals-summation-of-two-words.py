class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        lv={"a":"0","b":"1","c":"2","d":"3","e":"4","f":"5","g":"6","h":"7","i":"8","j":"9"}
        w=[firstWord,secondWord,targetWord]
        a=[]
        v=""
        for x in w:
            a.append(v)
            v=""
            for y in x:
                v+=lv[y]
        a.append(v)
        a.pop(0)
        fw=int(a[0])
        sw=int(a[1])
        tw=int(a[2])

        if fw+sw==tw:
            return(True)
        else:
            return(False)


        