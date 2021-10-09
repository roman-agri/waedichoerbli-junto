from datetime import datetime, timedelta
from waedichoerbli import settings

def get_delivery_dates_of_month(delivery_weekday, relative_month):
    today = datetime.today()
    # get dates of next month if this month is half over.
    month = (today.month + int(today.day > 15) + relative_month - 1) % 12 + 1
    date = datetime(today.year, month, 1)
    next_delivery = date + timedelta(days=(delivery_weekday - 1 - date.weekday()) % 7)
    yield next_delivery
    while True:
        next_delivery = next_delivery + timedelta(days=7)
        if next_delivery.month == month:
            yield next_delivery
        else:
            break
