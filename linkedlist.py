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
                cur.next =ListNode(list1.val) #create additional list 
                list1=list1.next
            else:
                cur.next =ListNode(list2.val)
                list2=list2.next
            cur=cur.next
        
        if list1: # attach tails if exist
            cur.next=list1
        if list2:
            cur.next=list2
            
        return dummy.next
# 141. Linked List Cycle

def hascycle(head):
        if not head or not head.next:
            return False
    
        slow, fast = head, head.next
        while fast and fast.next: #note the stop condition !
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        
        return False

# 2. Add Two Numbers

def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    
    carry =0
    _sum=ListNode(0) #learning create listnode
    dummy=_sum

    while l1 or l2 or carry:
        l1val=l1.val if l1 else 0 
        l2val=l2.val if l2 else 0              

        val=l1val+l2val+carry #carry logic
        carry=(val)//10
        nodeVal=val%10

        _sum.next =ListNode(nodeVal) #create next empty listnode

        _sum=_sum.next
        l1=l1.next if l1 else None

        l2=l2.next if l2 else None

    return dummy.next

#143. Reorder List

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        first=head
        slow, fast=head, head.next
        while fast and fast.next: #need this so slow.next 1, 2 x 3, 4
            slow=slow.next
            fast=fast.next.next
        
        second =slow.next
        #how to cut the end of first

        slow.next= None
        pre=None
        while second:
            next=second.next
            second.next=pre
            pre=second
            second =next
        # pre is the head of the second

        #merge
        dummy=first
        first, second=head, pre
        while second:
            temp1 = first.next
            first.next=second
            first=temp1

            temp2 = second.next
            second.next=first
            second=temp2
        
        return dummy
