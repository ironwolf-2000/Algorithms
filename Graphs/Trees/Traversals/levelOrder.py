from collections import deque


class TreeNode:
    def __init__(self, val=0, children=[]):
        self.val = val
        self.children = children


def levelOrder(root: TreeNode | None) -> list[int]:
    """
    N = number of nodes in the tree
    -------------
    Time: O(N)
    Space: O(N)
    """
    if not root:
        return []

    res = []
    q = deque([root])

    while q:
        node = q.popleft()
        res.append(node.val)

        for child in node.children:
            q.append(child)

    return res


root = TreeNode(1, [TreeNode(2, [TreeNode(3)]), TreeNode(5, [TreeNode(8), TreeNode(4)]), TreeNode(7)])
print(levelOrder(root))  # [1, 2, 5, 7, 3, 8, 4]

root = TreeNode(1, [TreeNode(2), TreeNode(3), TreeNode(4), TreeNode(5)])
print(levelOrder(root))  # [1, 2, 3, 4, 5]

root = None
print(levelOrder(root))  # []
