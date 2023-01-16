# Morris traversal works only for binary trees
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorderTraversal(root: TreeNode | None) -> list[int]:
    """
    N = number of nodes in the tree
    -----------
    Time: O(N)
    Space: O(1)
    """
    res = []
    cur = root

    while cur:
        if not cur.left:
            res.append(cur.val)
            cur = cur.right
        else:
            last = cur.left

            while last.right and last.right != cur:
                last = last.right

            if last.right == cur:
                last.right = None
                cur = cur.right
            else:
                res.append(cur.val)
                last.right = cur
                cur = cur.left

    return res


root = TreeNode(
    1, TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(6), TreeNode(7))), TreeNode(3, TreeNode(8), TreeNode(9))
)

print(preorderTraversal(root))  # [1, 2, 4, 5, 6, 7, 3, 8, 9]
