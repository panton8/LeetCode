#class ListNode:
    #def __init__(self, val=0, next = None):
        #self.val = val
        #self.next = next

def swapPairs(head: ListNode) -> ListNode:
    if head is None or head.next is None:
        return head

    pair_start = head
    new_head = head.next

    while True:
        nextNode = pair_start.next
        temp = nextNode.next
        nextNode.next = pair_start

        if temp is None or temp.next is None:
            pair_start.next = temp
            break

        pair_start.next = temp.next
        pair_start = temp

    return new_head
