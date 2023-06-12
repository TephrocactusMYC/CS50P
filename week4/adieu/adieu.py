import inflect
def main():
    p = inflect.engine()
    names = []
    while True:
        try:
            name=input("Name: ").strip()
            names.append(name)
        except EOFError:
            print()
            break
    print(f"Adieu, adieu, to {p.join(names)}")
main()