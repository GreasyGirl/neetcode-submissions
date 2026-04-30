# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: 
            return True
        if not p or not q: 
            return False
        
        pQueue = deque([p])
        qQueue = deque([q])

        while pQueue and qQueue: 
            
            #deque node 
            node1 = pQueue.popleft()
        
            node2 = qQueue.popleft()
            if node1 is None and node2 is None: 
                continue #skip the current cycle
            if node1 is None or node2 is None:
                return False 
            #both nodes are not none
            if node1.val != node2.val:
                return False
            
            #append children 
            pQueue.append(node1.left)
            pQueue.append(node1.right)
            qQueue.append(node2.left)
            qQueue.append(node2.right)


        return True
        




       