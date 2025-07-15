'''LeetCode 热题 100 —— 021.合并两个有序链表 - Easy'''

# 递归法
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        # 递归方法
        # 递归结束条件，否则会死循环
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        # 如果list1的值更小，就把list1作为新链表当前节点，然后去递归合并list1.next和list2
        # self指内部调用，指当前这个类的实例对象
        while list1 and list2:
            if list1.val < list2.val:
                list1.next = self.mergeTwoLists(list1.next, list2)
                return list1
            else:
                list2.next = self.mergeTwoLists(list1, list2.next)
                return list2
            
        # 非递归方法，需要一个哑节点（dummy node），用来构建新链表的起点
        dummy = ListNode(-1)
        current = dummy # 哑节点指针，用来一直往后拼接新的节点
        
        # 当两个链表都不为空，逐个比较节点大小
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1 # 小的那个挂到 current 后面
                list1 = list1.next
            else:
                current.next = list2 # 小的那个挂到 current 后面
                list2 = list2.next
            current = current.next # 当前指针向后移动
        
        # 处理剩下的链表（其中一个可能还没有处理完）
        if list1:
            current.next = list1
        if list2:
            current.next = list2
        
        # 返回合并后的链表，去掉 dummy 节点本身
        return dummy.next
        
        
        