# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q=[]
        if root is None:
            return 0
        q.append(root)
        level=[]
        cnt=0
        while len(q)>0:
            cnt+=1
            for i in range(len(q)):
                parent=q.pop(0)
                if parent is None:
                    continue
                if parent.left:
                    q.append(parent.left)
                if parent.right:
                    q.append(parent.right)
        
        return cnt
            
        