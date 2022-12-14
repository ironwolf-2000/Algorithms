class TreeNode:
    def __init__(self, val=0, children=[]):
        self.val = val
        self.children = children


# v1: recursive
def preorderR(root: TreeNode | None) -> list[int]:
    """
    N = number of nodes in the tree
    H = height of the tree
    -------------
    Time: O(N)
    Space: O(H)
    """

    def preorder(root: TreeNode | None) -> list[int]:
        if root:
            res.append(root.val)
            for child in root.children:
                preorder(child)

    res = []
    preorder(root)
    return res


# v2: iterative
def preorderI(root: TreeNode | None) -> list[int]:
    """
    N = number of nodes in the tree
    -------------
    Time: O(N)
    Space: O(N)
    """
    stack = [root]
    res = []

    while stack:
        node = stack.pop()
        if node:
            res.append(node.val)
            for child in reversed(node.children):
                stack.append(child)

    return res


root = TreeNode(7, [TreeNode(1), TreeNode(2, [TreeNode(0), TreeNode(3, [TreeNode(6)])]), TreeNode(4, [TreeNode(5)])])
print(preorderR(root))  # [7, 1, 2, 0, 3, 6, 4, 5]
print(preorderI(root))  # [7, 1, 2, 0, 3, 6, 4, 5]

root = TreeNode(1, [TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5)])
print(preorderR(root))  # [1, 2, 3, 4, 5]
print(preorderI(root))  # [1, 2, 3, 4, 5]

root = None
print(preorderR(root))  # []
print(preorderI(root))  # []
