# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        result=[]
        level=[]
        result.append([root])
        q=[]
        q.append(root)
        while len(q)>0:
            n=len(q)
            level=[]
            for i in range(len(q)):
                parent=q.pop(0)
                if parent:
                    parent.left,parent.right=parent.right,parent.left
                else:
                    continue
                
                if parent.left:
                    q.append(parent.left)
                if parent.right:
                    q.append(parent.right)
                    
        return root

            
        
        