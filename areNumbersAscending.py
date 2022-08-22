def areNumbersAscending(s: str) -> bool:
    numbers = []
    num = ''
    index = 0
    for i in range(len(s)):
        if s[i] >= '0' and s[i] <= '9':
            num += s[i]
            if s[i+1] >= '0' and s[i + 1] <= '9':
                continue
            else:
                numbers.append(int(num))
                index += 1
                num = ''

    for i in range(len(numbers)-1):
        if numbers[i] < numbers[i+1]:
            continue
        else:
            return False

    return True
