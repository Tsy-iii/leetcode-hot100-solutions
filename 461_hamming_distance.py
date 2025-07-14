'''LeetCode 热题 100 —— 461.汉明距离 - Easy'''

# 方法1：位运算，异或运算
# 时间复杂度：O(n)
# 空间复杂度：O(1)

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        # 异或运算，相同为0，不同为1
        return bin(x ^ y).count('1')
    
# 方法2：循环，每次取出x和y的最后一位，统计不相同的位数
# 时间复杂度：O(n)
# 空间复杂度：O(1)

class Solution(object):
    def hammingDistance(self, x, y):        
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        count = 0
        # 循环，直到x和y都为0
        while x or y:
            # 取出x和y的最后一位
            bit_x = x & 1
            bit_y = y & 1
            # 如果不相同，则计数
            if bit_x != bit_y:
                count += 1
            # 左移一位，并更新x和y
            x >>= 1
            y >>= 1
        return count