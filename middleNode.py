#class ListNode:
    #def __init__(self, val=0, next=None):
        #self.val = val
        #self.next = next

def middleNode(head: ListNode) -> ListNode:
        len = 0
        copy = head
        while head:
            len += 1
            head = head.next
        mid_index = len // 2
        count = 0
        new_one = ListNode()
        res = new_one
        while len:
            if count >= mid_index:
                new_one.val = copy.val
                if len > 1:
                    temp = ListNode()
                    new_one.next = temp
                    new_one = new_one.next
            copy = copy.next
            count += 1
            len -= 1
        return res