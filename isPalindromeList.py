# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def isPalindromeList(head) -> bool:
    sequence = ""

    while head:
        sequence += str(head.val)
        head = head.next

    if sequence == sequence[::-1]:
        return True

    return False
