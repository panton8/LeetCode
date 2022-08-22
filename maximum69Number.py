def maximum69Number (num: int) -> int:
    num_str = str(num)
    numbers = [num_str] * len(num_str)
    index = 0

    for num in numbers:
        if num[index] == '9':
            num = num[:index] + '6' + num[index + 1:]
            numbers.pop(index)
            numbers.insert(index, num)
        else:
            num = num[:index] + '9' + num[index + 1:]
            numbers.pop(index)
            numbers.insert(index, num)
        index += 1
    numbers.append(num_str)
    all_num = []

    for num in numbers:
        all_num.append(int(num))

    return max(all_num)
