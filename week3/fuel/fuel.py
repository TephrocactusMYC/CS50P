def main():
    while True:
        try:
            x, y = map(int, input("Fraction: ").split("/"))
            percentage = round(x / y * 100)
            if x>y:
                raise ValueError
            elif percentage <= 1:
                print("E")
                return 0
            elif percentage >= 99:
                print("F")
                return 0
            else:
                print(f"{percentage}%")
                return 0
        except (ValueError, ZeroDivisionError):
            pass

main()