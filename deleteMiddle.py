#class ListNode:
     #def __init__(self, val=0, next=None):
         #self.val = val
         #self.next = next

def deleteMiddle(head: ListNode) -> ListNode:
    copy_head = new_head = head
    list_len = 0

    while copy_head:
        list_len += 1
        copy_head = copy_head.next

    mid = list_len // 2

    if list_len == 1:
        head = None
        return head
    else:
        count = 0
        while head:
            if count + 1 == mid:
                head.next = head.next.next
                break
            count += 1
            head = head.next

    return new_head

