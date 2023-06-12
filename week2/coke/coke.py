def main():
    amount=50
    print("Amount Due:",amount)
    while amount>0:
        coin=int(input("Insert Coin: "))
        if coin in (25,10,5):
            amount-=coin
            if amount>0:
                print("Amount Due:",amount)
            else:
                print("Change Owed:",-amount)
        else:
            print("Amount Due:",amount)

main()