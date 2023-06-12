def main():
    time = input("What time is it? ")
    time = convert(time)
    if 7<=time and time<=8:
        print("breakfast time")
    elif 12<=time and time<=13:
        print("lunch time")
    elif 18<=time and time<=19:
        print("dinner time")
    else:
        pass

def convert(time):
    hours, minutes = map(float,time.split(":"))
    minutes = minutes / 60
    return hours+minutes

if __name__ == "__main__":
    main()