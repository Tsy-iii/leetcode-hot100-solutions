'''LeetCode 热题 100 —— 160.相交链表 - Easy'''
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 🔸 时间复杂度：O(m + n)
# 	•	m：链表 A 的长度
# 	•	n：链表 B 的长度
# 	•	第一步分别遍历 A 和 B 获取长度，耗时 O(m + n)
# 	•	第二步让较长链表先走长度差 |m - n|，再一起走，最多 O(m) 或 O(n)
# 	•	所以总共 只走了两遍链表：O(m + n)

# ⸻

# 🔸 空间复杂度：O(1)
# 	•	只用了若干变量（比如 lengthA、lengthB、len、指针 listA、listB），不使用任何额外数据结构
# 	•	所以 是原地算法，空间复杂度为常数级：O(1)
 
class Solution:
    def getIntersectionNode(self, headA, headB):
        lengthA = lengthB = 0
        listA, listB = headA, headB
        # 求链表A的长度
        while listA is not None:
            lengthA += 1
            listA = listA.next
        # 求链表B的长度
        while listB is not None:
            lengthB += 1
            listB = listB.next
        # 链表头重置 !!!!!!!!!!!!!!!!!!
        listA, listB = headA, headB
        # 将链表A作为长链表
        if lengthB > lengthA:
            lengthA, lengthB = lengthB, lengthA
            listA, listB = listB, listA
        # 求链表长度的差
        len = lengthA - lengthB
        # 将长链表A起点与短链表B起点并起
        while len != 0:
            listA = listA.next
            len -= 1
        # 链表A和链表B同起点，现在开始比较是否为相同节点，即是否相交
        while listA is not None:
            if listA == listB:
                return listA
            else:
                listA = listA.next
                listB = listB.next
        return None
    
        
        

        
        