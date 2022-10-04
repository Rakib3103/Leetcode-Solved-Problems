#Using Kadane's Algorithm
#-----------------------------------------------------------------------------------------------------#
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        Max = nums[0]
        Sum = 0
        
        for i in nums:
            Sum += i
            Max = max(Max, Sum)
            if Sum < 0:
                Sum = 0
        return Max

        
        
