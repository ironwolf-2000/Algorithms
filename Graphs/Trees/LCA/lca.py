# Lowest Common Ancestor (LCA) in a Binary Tree


class TreeNode:
    def __init__(self, val: int, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def lca(root: TreeNode | None, p: TreeNode, q: TreeNode) -> TreeNode | None:
    """
    N = number of nodes in the tree
    H = height of the tree
    ------------
    Time: O(N)
    Space: O(H)
    """
    if not root or root in (p, q):
        return root

    left = lca(root.left, p, q)
    right = lca(root.right, p, q)

    if left and right:
        return root

    return left or right


p2 = TreeNode(2)
p4 = TreeNode(4)
p6 = TreeNode(6)
root = TreeNode(0, TreeNode(1, p2, TreeNode(3, p4, TreeNode(5, p6))))

print(lca(root, p2, p4).val)  # 1
print(lca(root, p6, root).val)  # 0
print(lca(root, root, p6).val)  # 0
