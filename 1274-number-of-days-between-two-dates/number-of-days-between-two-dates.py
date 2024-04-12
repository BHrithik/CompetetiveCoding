class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:

        def is_leap_year(year: int) -> bool:
            return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

        def get_days(date: str) -> int:
            y, m, d = map(int, date.split('-'))

            days = d + int(is_leap_year(y) and m > 2)
            days += sum(365 + int(is_leap_year(y)) for y in range(1971, y))
            days += sum([0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][:m])

            return days

        day1 = int(date1.split('-')[2])
        day2 = int(date2.split('-')[2])
        month1 = int(date1.split('-')[1])
        month2 = int(date2.split('-')[1])
        year1 = int(date1.split('-')[0])
        year2 = int(date2.split('-')[0])

        return abs(get_days(date1) - get_days(date2))
            