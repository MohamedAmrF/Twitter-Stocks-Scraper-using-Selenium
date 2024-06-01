from datetime import datetime, timedelta

def convert_minutes_to_date(minutes):
    start_date = datetime(year=2006, month=1, day=1)
    delta = timedelta(minutes=minutes)
    new_date = start_date + delta
    return new_date

def convert_date_to_minutes(date):
    start_date = datetime(year=2006, month=1, day=1)
    delta = date - start_date
    return delta.total_seconds() / 60