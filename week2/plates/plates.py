def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s)<2 or len(s)>6:
        return False
    if s[0].isalpha()!=1 or s[1].isalpha()!=1:
        return False
    if s.isalnum()!=1:
        return False
    for c in s:
        if c.isdigit():
            if c=="0":
                return False
            if not s[s.index(c):].isnumeric():
                return False
            break
    else:
        return True
    return True

main()