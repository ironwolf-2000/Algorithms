# Morris traversal works only for binary trees
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def postorderTraversal(root: TreeNode | None) -> list[int]:
    """
    N = number of nodes in the tree
    -----------
    Time: O(N)
    Space: O(1)
    """
    res = []
    cur = root

    while cur:
        if not cur.right:
            res.append(cur.val)
            cur = cur.left
        else:
            last = cur.right

            while last.left and last.left != cur:
                last = last.left

            if last.left == cur:
                last.left = None
                cur = cur.left
            else:
                res.append(cur.val)
                last.left = cur
                cur = cur.right

    res.reverse()
    return res


root = TreeNode(
    1, TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(6), TreeNode(7))), TreeNode(3, TreeNode(8), TreeNode(9))
)

print(postorderTraversal(root))  # [4, 6, 7, 5, 2, 8, 9, 3, 1]
