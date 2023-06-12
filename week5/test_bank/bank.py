def main():
    x=input("Greeting: ").strip().title()
    print(f"${value(x)}")

def value(greeting):
    if greeting[0:5]=="Hello":
        return 0
    elif greeting[0]=="H":
        return 20
    else:
        return 100
if __name__ == "__main__":
    main()