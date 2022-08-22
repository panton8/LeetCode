#class ListNode:
     #def __init__(self, val=0, next=None):
         #self.val = val
         #self.next = next

def reverseBetween(head: ListNode, left: int, right: int) -> ListNode:
    if left == right:
        return head

    copy_list = head
    reverse_list = []
    count = 1

    while copy_list:
        if count >= left and count <= right:
            reverse_list.append(copy_list.val)
        count += 1
        copy_list = copy_list.next

    count = 1
    res = head
    reverse_list.reverse()
    index = 0

    while head:
        if count >= left and count <= right:
            head.val = reverse_list[index]
            index += 1
        count += 1
        head = head.next

    return res
