def dayOfYear(date: str) -> int:
    days_per_month = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    total_days = 0

    for month in range(int(date[5:7]) - 1):
        total_days += days_per_month[month + 1]

    total_days += int(date[8:])

    if int(date[:4]) % 4 == 0 and int(date[5:7]) > 2:
        if int(date[:4]) % 100 == 0 and int(date[:4]) % 400 == 0:
            total_days += 1
        elif int(date[:4]) % 100 != 0:
            total_days += 1

    return total_days


def main():
    print(dayOfYear("1900-05-02"))


if __name__ == "__main__":
    main()
