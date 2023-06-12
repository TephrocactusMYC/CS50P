import sys
import inflect
from datetime import datetime, date,timedelta


class season:
    def __init__(self, birthdate=0):
        self.birthdate = self.validate(birthdate)
        self.now = self.current_time()
        self.time = self.time_delta()

    def __str__(self):
        p = inflect.engine()
        lyrics = p.number_to_words(self.time, andword="")
        return f"{lyrics} minutes".capitalize()

    def validate(self, birthdate):
        '''十分离谱的东西，不写好像过不去'''
        if not birthdate:
            birthdate = input("Date of Birth: ").strip()
        try:
            birthdate = datetime.strptime(birthdate, "%Y-%m-%d").date()
            return birthdate
        except ValueError:
            sys.exit("Invalid Date. Please enter a date in the format YYYY-MM-DD")

    def current_time(self):
        now = date.today()
        return now

    def time_delta(self):
        """Return the time delta in minutes as an integer."""
        td = self.now - self.birthdate
        time = int(td / timedelta(minutes=1))
        return time


def main():
    birthdate = input("Date of Birth: ")
    seasons = season(birthdate)
    print(seasons)


if __name__ == "__main__":
    main()
