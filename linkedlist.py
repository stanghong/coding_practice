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

# 21. Merge Two Sorted Lists
        
       dummy=ListNode()
        cur=dummy

        while list1 and list2:
            if list1.val<=list2.val:
                cur.next =ListNode(list1.val)
                list1=list1.next
            else:
                cur.next =ListNode(list2.val)
                list2=list2.next
            cur=cur.next
        
        if list1:
            cur.next=list1
        if list2:
            cur.next=list2
            
        return dummy.next
# 141. Linked List Cycle

def hascycle(head):
        if not head or not head.next:
            return False
    
        slow, fast = head, head.next
        while fast and fast.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        
        return False
