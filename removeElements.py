#class ListNode:
    #def __init__(self, val=0, next=None):
        #self.val = val
        #self.next = next

def removeElements(head: ListNode, val: int) -> ListNode:
    if not head:
        return head

    while head.val == val:
        head = head.next

    new_head = head

    while head:
        if head.next and head.next.val == val:
            while head.next.val == val:
                head.next = head.next.next
            head = head.next
        else:
            head = head.next

    return new_head