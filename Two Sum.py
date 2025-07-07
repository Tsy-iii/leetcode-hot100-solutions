'''LeetCode 热题 100 —— 1.两数之和'''

# 方法一：暴力法
# 思路及算法
# 最容易想到的方法是枚举数组中的每一个数 x，寻找数组中是否存在 target - x
# 当我们使用遍历整个数组的方式寻找 target - x 时，需要注意到每一个位于 x 之前的元素都已经和 x 匹配过，因此不需要再进行匹配
# 而每一个元素不能被使用两次，所以我们只需要在 x 后面的元素中寻找 target - x

# 复杂度分析
# 时间复杂度：O(N^2)，其中 N 是数组中的元素数量。最坏情况下数组中任意两个数都要被匹配一次
# 空间复杂度：O(1)

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range (len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return[i, j]
                
# 方法二：哈希表
# 思路及算法
# 我们可以将数组中的元素存入哈希表中，然后遍历数组中的每一个元素 x，寻找 target - x 是否存在于哈希表中
# 如果存在，则找到了对应的元素，返回其索引和 x 的索引
# 如果不存在，则将 x 存入哈希表中

# 复杂度分析    
# 时间复杂度：O(N)，其中 N 是数组中的元素数量。遍历数组一次，哈希表操作一次
# 空间复杂度：O(N)，哈希表的大小为 N

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashMap = {} # 用来存储已经遍历过的数和它们的索引
        
        # 用 enumerate 写
        for i, num in enumerate(nums): # 遍历数组，同时获取索引和值（它会把 nums 变成一个带索引的可迭代对象）
            another = target - num
            if another in hashMap:  # 如果存在 target - num，则找到了对应的元素，返回其索引和 x 的索引
                return [hashMap[another], i]
            hashMap[num] = i # 将当前数存入哈希表中，同时记录它的索引
        return [] # 如果没有找到对应的元素，则返回空列表
    
        # 不用 enumerate 写
        # for i in range(len(nums)):
        #     num = nums[i]
        #     if target - num in hashmap:
        #         return [hashmap[target - num], i]
        #     hashmap[num] = i
        # return []
        
        
        
        