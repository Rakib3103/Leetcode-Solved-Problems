# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []     #Taking a empty list
        
#Initializing the queue
        queue = collections.deque()
        queue.append(root)
        
#Iteration over the queue until it becomes empty
        while queue:
            queue_length = len(queue)       #Showing that we are going through 1 level at a time
            level = []
            
#Loop through every value of the list
            for i in range(queue_length):
                node = queue.popleft()      #First IN First OUT
                
#For ensuring not Null
                if node:
                    level.append(node.val)
                    
#For appending the childrens
                    queue.append(node.left)
                    queue.append(node.right)

#To make sure if the level is not empty
            if level:
                result.append(level)

        return result
        