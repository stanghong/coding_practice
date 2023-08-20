# 206. Reverse Linked List
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #iteratively two pointer pre, yellow
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

# recursion: not required, 
        # note: cur.next.next = cur and cur.next=None 
        # and learn how to write recursion 
        if head ==None or head.next==None:
            return head

        def flip(cur):
            if not cur.next:
                return cur
            newhead=flip(cur.next)
            cur.next.next =cur
            cur.next=None
            return newhead

        return flip(head)
        
