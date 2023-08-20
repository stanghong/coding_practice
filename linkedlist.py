# 206. Reverse Linked List
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #iteratively two pointer pre
        #     1->2->3
        #pre  cur
        pre = None
        cur =head
        while cur:
            temp=cur.next
            cur.next=pre
            pre = cur
            cur = temp
        return pre
        
