def main():
    food = {}
    while True:
        try:
            item = input().upper()
            if item not in food:
                food[item] = 1
            else:
                food[item] += 1

        except EOFError:
            print()
            break
    for key,value in sorted(food.items()):
        print(value,key)

main()
