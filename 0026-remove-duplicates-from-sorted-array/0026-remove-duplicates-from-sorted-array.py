class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=0
        for i in range(len(nums)):
            if nums[i] > nums[k]:
                nums[k+1] , nums[i] = nums[i] , nums[k+1]
                k+=1
        return(k+1)


        