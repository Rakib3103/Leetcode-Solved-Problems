class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        if k == len(nums):
            return nums
        
        counts = Counter(nums)          #A subclass of dict that's specially designed for counting hashable objects in Python
        
        return heapq.nlargest(k,counts.keys(), key = counts.get)        #The get method on a dictionary returns the value stored in a key, or optionally, a default value, specified by the optional second parameter. 
        