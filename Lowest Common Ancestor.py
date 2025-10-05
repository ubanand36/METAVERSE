# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowestCommonAncestor(root, p, q):
    # Base case
    if not root or root == p or root == q:
        return root

    # Search left and right subtrees
    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    # If both left and right are not None, current node is LCA
    if left and right:
        return root

    # Otherwise, return non-None side
    return left if left else right


# Example Tree
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)

p = root.left            # Node 5
q = root.right           # Node 1

ans = lowestCommonAncestor(root, p, q)
print(ans.val)  # Output: 3
