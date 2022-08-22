def romanToInt1(s: str) -> int:
    s = s + ' '
    num = 0
    for i in range(len(s)):
        if s[i] == 'I':
            if s[i + 1] != 'V' and s[i + 1] != 'X' and s[i + 1] != 'L' and s[i + 1] != 'C' and s[i + 1] != 'D' and s[
                i + 1] != 'M':
                num += 1
            else:
                num -= 1

        elif s[i] == 'V':
            if s[i + 1] != 'X' and s[i + 1] != 'L' and s[i + 1] != 'C' and s[i + 1] != 'D' and s[i + 1] != 'M':
                num += 5
            else:
                num -= 5

        elif s[i] == 'X':
            if s[i + 1] != 'L' and s[i + 1] != 'C' and s[i + 1] != 'D' and s[i + 1] != 'M':
                num += 10
            else:
                num -= 10

        elif s[i] == 'L':
            if s[i + 1] != 'C' and s[i + 1] != 'D' and s[i + 1] != 'M':
                num += 50
            else:
                num -= 50

        elif s[i] == 'C':
            if s[i + 1] != 'D' and s[i + 1] != 'M':
                num += 100
            else:
                num -= 100

        elif s[i] == 'D':
            if s[i + 1] != 'M':
                num += 500
            else:
                num -= 500

        elif s[i] == 'M':
            num += 1000

    return num


def romanToInt2(s: str) -> int:
    conformity = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': -2, 'IX': -2, 'XL': -20,
                  'XC': -20, 'CD': -200, 'CM': -200}
    num = 0

    for key, value in conformity.items():
        num += s.count(key) * value

    return num
