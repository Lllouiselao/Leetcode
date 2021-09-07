"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    # 求出路径的 所有到leaf
    def binaryTreePaths(self, root):
        if root is None:
            return []
        # 如果只有一个node 可能性
        if root.left == None and root.right == None:
            return [str(root.val)]
        
        #拆左右子树
        leftPath = self.binaryTreePaths(root.left)
        rightPath = self.binaryTreePaths(root.right)

        paths = []
        for path in leftPath + rightPath:
            paths.append(str(root.val) + '->' +path)

        return paths