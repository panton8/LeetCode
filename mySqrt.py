def mySqrt(num: int) -> int:
    ans = 0
    square = 1

    while True:
        if square * square < num:
            ans = square
            square += 1
        elif square * square == num:
            return square
        elif square * square > num:
            return ans

def main():

    print(mySqrt(101))

if __name__ == "__main__":
    main()
