#class TreeNode:
    #def __init__(self, val=0, left=None, right=None):
         #self.val = val
         #self.left = left
         #self.right = right

def checkTree(root: TreeNode) -> bool:
    return root.val == root.right.val + root.left.val


