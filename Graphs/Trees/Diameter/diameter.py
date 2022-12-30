class TreeNode:
    def __init__(self, val=0, children=[]):
        self.val = val
        self.children = children


def getDiameter(root: TreeNode | None) -> int:
    """
    N = number of nodes in the tree
    -------------
    Time: O(N)
    Space: O(N)
    """

    def dfs(root: TreeNode | None) -> tuple[int, int]:
        if not root:
            return -1, 0

        mx_h1, mx_h2, mx_res = -1, -1, 0
        for child in root.children:
            h, r = dfs(child)
            if h > mx_h1:
                mx_h1, mx_h2 = h, mx_h1
            elif h > mx_h2:
                mx_h2 = h
            mx_res = max(mx_res, r)

        return mx_h1 + 1, max(mx_res, mx_h1 + mx_h2 + 2)

    return dfs(root)[1]


#    1
#     \
#      3
#     /|\
#    4 5 6
#   / \   \
#  7   8   9

root = TreeNode(1, [TreeNode(3, [TreeNode(4, [TreeNode(7), TreeNode(8)]), TreeNode(5), TreeNode(6, [TreeNode(9)])])])
print(getDiameter(root))  # 4


#          1
#      / /   \ \
#     2 3     4 5
#             / | \
#            6  7  8
#            |  |  |
#            9 10 11
#            |
#           12

root = TreeNode(
    1,
    [
        TreeNode(2),
        TreeNode(3),
        TreeNode(4),
        TreeNode(
            5, [TreeNode(6, [TreeNode(9, [TreeNode(12)])]), TreeNode(7, [TreeNode(10)]), TreeNode(8, [TreeNode(11)])]
        ),
    ],
)
print(getDiameter(root))  # 5
