#class ListNode:
    #def __init__(self, val=0, next=None):
        #self.val = val
        #self.next = next

def deleteDuplicates(head: ListNode) -> ListNode:
    without_dupl = head

    while head:
        if head.next:
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        else:
            head = head.next

    return without_dupl
