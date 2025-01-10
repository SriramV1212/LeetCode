class Solution(object):
    def majorityElement(self, nums):
        l=[]
        d={nums[0]:1}
        l.append(nums[0])

        for i in range(1,len(nums)):
            if nums[i] not in l:
                l.append(nums[i])
                d[nums[i]]=1
            else:
                x=d.get(nums[i])
                x+=1
                d[nums[i]]=x
        
        max=0
        for x in d.values():
            if x>max:
                max=x
        
        return(d.keys()[d.values().index(max)])
        