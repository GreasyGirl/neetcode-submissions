# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True 
        
        neg_inf = float('-inf')
        pos_inf = float('inf')
        
        q = deque([(root, neg_inf, pos_inf)])

        while q: 
            node, leftBound, rightBound = q.popleft()
            if not (leftBound < node.val < rightBound): 
                return False
            if node.left: #update rightBound
                q.append((node.left, leftBound, node.val))
            if node.right: #update leftBound
                q.append((node.right, node.val, rightBound))
                     
            

        return True 
