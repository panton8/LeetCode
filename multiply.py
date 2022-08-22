def multiply1(num1: str, num2: str) -> str:
    from_str_to_int = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    from_int_to_str = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}

    num1_to_int = 0
    num2_to_int = 0

    for i in range(len(num1)):
        num1_to_int += from_str_to_int.get(num1[i]) * (10 ** (len(num1) - i - 1))
    for i in range(len(num2)):
        num2_to_int += from_str_to_int.get(num2[i]) * (10 ** (len(num2) - i - 1))

    res_int = num1_to_int * num2_to_int
    res_str = ''

    if not res_int:
        res_str = '0'

    while res_int >= 1:
        res_str += from_int_to_str.get(res_int % 10)
        res_int //= 10

    return res_str[::-1]


def multiply2(num1: str, num2: str) -> str:
    num1_int = int(num1)
    num2_int = int(num2)
    return str(num2_int * num1_int)
