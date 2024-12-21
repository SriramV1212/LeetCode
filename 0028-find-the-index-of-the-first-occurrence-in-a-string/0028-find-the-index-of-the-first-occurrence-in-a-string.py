class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n = len(needle)
        h = len(haystack)
        List = []
        for i in range(h):
            z = haystack[i:i+n]
            if needle == z:
                List.append(i)

        if len(List)!=0:
            return(List[0])
        else:
            return(-1)
        