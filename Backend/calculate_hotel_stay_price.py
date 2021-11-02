import json
import sqlite3
import datetime
import re



def create_date(date_string):
    #CONSISTANT FORMAT yyyy-mm-dd : EXAMPLE: 2/4/2021 or 12/12/2021

    processed_date = re.search(r'([0-9]*)-([0-9]*)-([0-9]*)', date_string)


    month = int(processed_date.group(2))
    day = int(processed_date.group(3))
    year = int(processed_date.group(1))

    date = datetime.datetime(year,month,day)

    return date



def create_date_range(user_start_date,user_end_date):
    start = create_date(str(user_start_date))
    end = create_date(str(user_end_date))

    step = datetime.timedelta(days=1)

    date_range = []
    while start< end:
        date_range.append(start)
        start += step

    return date_range

def calculate_price(user_start_date,user_end_date,hotel_room_price,weekend_percent):
    user_date_range = create_date_range(user_start_date, user_end_date)

    num_days = len(user_date_range)
    sub_total_price = 0.0
    num_weekends = 0
    num_weekdays = 0
    weekday_price = 0.0
    weekend_price = 0.0
    for date in user_date_range:
        processed_date = create_date(str(date))
        if processed_date.date().weekday() < 5:
            sub_total_price += float(hotel_room_price)
            num_weekdays +=1
            weekday_price += float(hotel_room_price)
        else:
            sub_total_price += float(hotel_room_price)+(float(int(hotel_room_price) * float(int(weekend_percent)/100)))
            num_weekends+=1
            weekend_price += float(hotel_room_price)+(float(int(hotel_room_price) * float(int(weekend_percent)/100)))

    price_information = {}
    price_information[0] = {"NUM_DAYS":num_days, "NUM_WEEKDAYS":num_weekdays,"WEEKDAY_PRICE":weekday_price,"NUM_WEEKENDS":num_weekends,"WEEKEND_PRICE":weekend_price,"SUBTOTAL":sub_total_price}
    price_information_json = json.dumps(price_information)

    return price_information_json
