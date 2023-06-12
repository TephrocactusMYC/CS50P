def validate(ip):
    # split the ip into its components
    parts = ip.split(".")

    # check that there are only 4 parts
    if len(parts) != 4:
        return False

    # check that each part is an integer between 0 and 255
    for part in parts:
        if not part.isdigit() or int(part) < 0 or int(part) > 255:
            return False

    return True


def main():
    ip = input("IPv4 Address: ")
    if validate(ip):
        print("True")
    else:
        print("False")


if __name__ == "__main__":
    main()
