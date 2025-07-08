'''LeetCode 热题 100 —— 283.移动零 - Easy'''

# 方法1：双指针，开始都指向第一个元素，总共用了2次单独的遍历（因此不增加时间复杂度，还是O(n)）
# 时间复杂度：O(n)
# 空间复杂度：O(1)

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return 0
        # 第一次遍历的时候，j指针记录非0的个数，只要是非0的统统都赋给nums[j]	
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0: # 也可以简写为 if nums[i]:
                nums[j] = nums[i] # 直接赋值，因此有脏数据，后期需要清理用0填充
                j += 1
        # 非0元素统计完了，剩下的都是0了
		# 所以第二次遍历把末尾的元素都赋为0即可
        for i in range(j, len(nums)):
            nums[i] = 0
        return nums
    
# 方法2：双指针，开始都指向第一个元素，总共用了1次遍历
# 思路及解法
# 使用双指针，左指针指向当前已经处理好的序列的尾部，右指针指向待处理序列的头部。
# 右指针不断向右移动，每次右指针指向非零数，则将左右指针对应的数交换，同时左指针右移。

# 注意到以下性质：
# 左指针左边均为非零数；
# 右指针左边直到左指针处均为零。
# 因此每次交换，都是将左指针的零与右指针的非零数交换，且非零数的相对顺序并未改变。

# 复杂度分析
# 时间复杂度：O(n)，其中 n 为序列长度。每个位置至多被遍历两次。
# 空间复杂度：O(1)。只需要常数的空间存放若干变量。

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        left = right = 0 # 左右指针
        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left] # 直接交换，因此无脏数据，无需清理（少一次遍历）
                left += 1
            right += 1
        return nums
    
    