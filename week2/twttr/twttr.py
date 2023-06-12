def main():
    text=input("Input: ")
    print("Output: ",end="")
    for c in text:
        if c.lower() in "aeiou":
            pass
        else:
            print(c,end="")
    print()
main()