import datetime
def has_friday_13(month, year):
    date = datetime.date(year, month, 13)
    return date.weekday() == 4