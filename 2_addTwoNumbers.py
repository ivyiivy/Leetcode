class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution():
    def addTwoNumbers(self, l1, l2):
        """
               :type l1: ListNode
               :type l2: ListNodel
               :rtype: ListNode
               """
        rt= ListNode(0)
        r = rt
        carry = 0
        while (l1 or l2):
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            s = carry + x + y
            r.val = s % 10
            carry = s // 10
            r.next = ListNode(0)
            r=r.next
            l1 = l1.next
            l2 = l2.next
        return rt
