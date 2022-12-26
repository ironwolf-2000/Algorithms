class TreeNode:
    def __init__(self, val=0, children=[]):
        self.val = val
        self.children = children


# v1: recursive
def postorderR(root: TreeNode | None) -> list[int]:
    """
    N = number of nodes in the tree
    H = height of the tree
    -------------
    Time: O(N)
    Space: O(H)
    """

    def postorder(root: TreeNode | None) -> None:
        if root:
            for child in root.children:
                postorder(child)
            res.append(root.val)

    res = []
    postorder(root)
    return res


# v2: iterative
def postorderI(root: TreeNode | None) -> list[int]:
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
            for child in node.children:
                stack.append(child)

    return res[::-1]


root = TreeNode(7, [TreeNode(1), TreeNode(2, [TreeNode(0), TreeNode(3, [TreeNode(6)])]), TreeNode(4, [TreeNode(5)])])
print(postorderR(root))  # [1, 0, 6, 3, 2, 5, 4, 7]
print(postorderI(root))  # [1, 0, 6, 3, 2, 5, 4, 7]

root = TreeNode(1, [TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5)])
print(postorderR(root))  # [2, 3, 4, 5, 1]
print(postorderI(root))  # [2, 3, 4, 5, 1]

root = None
print(postorderR(root))  # []
print(postorderI(root))  # []
