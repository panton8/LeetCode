# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    copy_list = head
    reverse_list = []

    while copy_list:
        reverse_list.append(copy_list.val)
        copy_list = copy_list.next

    res = head
    reverse_list.reverse()
    index = 0

    while head:
        head.val = reverse_list[index]
        index += 1
        head = head.next

    return res