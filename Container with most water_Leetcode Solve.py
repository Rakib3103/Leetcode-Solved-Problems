class Solution:
    def maxArea(self, height: List[int]) -> int:

        #Using Linear Time Solution
        result = 0
        left, right = 0 , len(height)-1
        
        while left<right:
            area = (right - left) * min(height[left], height[right])
            result = max(result, area)
            
            if height[left] < height[right]:
                left += 1       #Starts with index 0
                                
            else:
                right -= 1      #Starts with index -1
                
        return result
    
#---------------------------------------------------------------------------------------------------------------------#
                
#         Using Brute Force
        
#         result = 0
#         for l in range(len(height)):                #l refers to left pointer
#             for r in range(l + 1, len(height)):
#                 area = (r-l) * min(height(l), height(r))  
#                 result = max(result, area)
#         return result
                
            