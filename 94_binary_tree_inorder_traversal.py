'''LeetCode 热题 100 —— 94.二叉树的中序遍历 - Easy'''

# 方法1：递归
# 时间复杂度：O(n)
# 空间复杂度：O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        result = []
        
        def traverse(node):
            # 递归终止条件
            if not node:
                return False
            # 左子树遍历
            traverse(node.left)
            # 访问节点,添加到结果 result 中
            result.append(node.val)
            # 右子树遍历
            traverse(node.right)
        # 调用递归函数
        traverse(root)
        # 返回结果
        return result
    
# 方法二: 栈 
# 时间复杂度：O(n)
# 空间复杂度：O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        # 如果没有节点，则返回空列表
        if not root:
            return []
        
        result = []
        stack = []
        current = root
        
        # 当前节点存在，或者栈不为空
        while current or stack:
            # 左子树遍历，先将左子树入栈，一直往左走，直到没有左子树，所以是 while
            while current:
                stack.append(current)
                current = current.left
            
            # 走到最左的左子树，开始弹出栈顶节点
            current = stack.pop()
            # 弹出的节点，添加到结果 result 中
            result.append(current.val)
            # 接着往右子树遍历，如上同逻辑
            current = current.right
        
        return result