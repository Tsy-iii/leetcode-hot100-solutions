'''LeetCode 热题 100 —— 020.有效的括号 - Easy'''

# 栈和哈希表
# 时间复杂度：O(n)，其中 n 是字符串 s 的长度。
# 空间复杂度：O(n+∣Σ∣)，其中 ∣Σ∣ 是字符集的大小。

# 思路：
# 1. 创建一个空栈 stack。
# 2. 创建一个哈希表 pairs，用于存储右括号和对应的左括号。
# 3. 遍历字符串 s，如果遇到右括号，判断栈顶是否为对应的左括号。
# 4. 如果栈为空，或者栈顶元素不为对应的左括号，则返回 False。
# 5. 如果栈顶元素为对应的左括号，则出栈。
# 6. 如果遍历完字符串 s，栈为空，则返回 True。

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 用栈存储左括号，先创建个空栈
        stack = list()
        
        # 用哈希存储括号，key为右括号
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{',
        }
        
        # 字符串为奇数时，可以直接返回 False
        if len(s) % 2 == 1:
            return False
        
        # 开始遍历字符串
        for ch in s:
            # 如果遇到右括号,判断栈顶是否为对应的左括号
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]: # 想匹配时，栈空了，或者没得匹配，直接返回 False
                    return False
                stack.pop()  # 栈顶元素出栈(右括号匹配成功,消掉)
            # 如果遇到左括号
            else:
                stack.append(ch)  # 左括号入栈
        
        # 如果栈为空，说明括号匹配成功
        return not stack