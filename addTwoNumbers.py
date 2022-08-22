def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    num1 = 0
    digit = 1
    while l1:
        num1 += digit * l1.val
        l1 = l1.next
        digit *= 10

    num2 = 0
    digit = 1
    while l2:
        num2 += digit * l2.val
        l2 = l2.next
        digit *= 10

    sum = num2 + num1

    temp_res = ListNode()
    res = temp_res
    while sum >= 1:
        temp_res.val = sum % 10
        sum //= 10
        if sum >= 1:
            temp = ListNode()
            temp_res.next = temp
            temp_res = temp_res.next

    return res
