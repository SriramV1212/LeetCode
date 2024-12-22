class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        s=0
        a=0
        for j in range(len(nums)) :
            if nums[j]==1:
                a+=1
            else:
                if a>s:
                    s=a
                a=0
        if s>a:        
          return(s)
        else:
          return(a)

                
        