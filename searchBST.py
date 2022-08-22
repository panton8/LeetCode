#class TreeNode:
    #def __init__(self, val=0, left=None, right=None):
         #self.val = val
         #self.left = left
         #self.right = right

def searchBST(root: TreeNode, val: int) -> TreeNode:
        if root.val == val or root is None:
            return root
        if root.val < val:
            return searchBST(root.right, val)
        else:
            return searchBST(root.left, val)
