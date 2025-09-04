class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for i in range(len(nums)):
            if(nums[i] in d):
                d[nums[i]] = d.get(nums[i]) + 1
            else:
                d[nums[i]] = 1
            
            if(d[nums[i]] > len(nums) / 2):
                return(nums[i])
            
        return(-1)
