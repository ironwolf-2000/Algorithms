# This traversal works only for binary trees
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# v1: recursive
def inorderR(root: TreeNode | None) -> list[int]:
    """
    N = number of nodes in the tree
    H = height of the tree
    -------------
    Time: O(N)
    Space: O(H)
    """

    def inorder(root: TreeNode | None) -> None:
        if root:
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

    res = []
    inorder(root)
    return res


# v2: iterative
def inorderI(root: TreeNode | None) -> list[int]:
    """
    N = number of nodes in the tree
    H = height of the tree
    -------------
    Time: O(N)
    Space: O(H)
    """
    stack, res = [], []
    cur = root

    while stack or cur:
        while cur:
            stack.append(cur)
            cur = cur.left
        node = stack.pop()
        res.append(node.val)
        cur = node.right

    return res


root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6, TreeNode(5))))
print(inorderR(root))  # [1, 2, 3, 4, 5, 6, 7]
print(inorderI(root))  # [1, 2, 3, 4, 5, 6, 7]

root = None
print(inorderR(root))  # []
print(inorderI(root))  # []
