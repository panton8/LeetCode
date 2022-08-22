#class ListNode:
    #def __init__(self, val=0, next=None):
         #self.val = val
         #self.next = next

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    list_len = 0
    copy_head = new_head = head

    while copy_head:
        list_len += 1
        copy_head = copy_head.next

    from_head = list_len - n

    if from_head == 0:
        head = head.next
        return head
    else:
        while head:
            from_head -= 1

            if from_head == 0:
                head.next = head.next.next
            head = head.next

    return new_head
