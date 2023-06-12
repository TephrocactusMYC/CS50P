def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]
    while True:
        try:
            text = input("Date: ")
            if "/" in text:
                month,day,year=map(int,text.split("/"))
                if 1<=month and month<=12 and 1<=day and day<=31:
                    print(f"{year:04d}-{month:02d}-{day:02d}")
                    return 0
            if " " in text and "," in text:
                text=text.replace(",","")
                month,day,year=text.split(" ")
                day=int(day)
                year=int(year)
                if month in months and 1<=day and day<=31:
                    print(f"{year:04d}-{months.index(month)+1:02d}-{day:02d}")
                    return 0
        except ValueError:
            pass


main()
