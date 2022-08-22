class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def mergeTwoLists(list1:ListNode, list2: ListNode) -> ListNode:
    arr = []
    while list1:
        arr.append(list1.val)
        list1 = list1.next

    while list2:
        arr.append(list2.val)
        list2 = list2.next

    if arr:
        arr.sort()
        res = ListNode()
        ans = res

        for i in range(len(arr)):
            res.val = arr[i]
            if i != len(arr) - 1:
                temp = ListNode()
                res.next = temp
                res = res.next

        return ans
    else:
        return
