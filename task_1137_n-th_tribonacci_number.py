def tribonacci(n: int) -> int:
    if n == 0:
        return 0
    a, b, c = 0, 1, 1

    for i in range(3, n + 1):
        a, b, c = b, c, a + b + c
    return c



def main():
    print(tribonacci(25))


if __name__ == "__main__":
    main()
