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

def is_room_type_available(conn,HID,room_type,num_of_rooms,user_start_date,user_end_date):
    # out of total num rooms = 50% will be standard , 30% will be Queen, and 20% will be King = 100% total

    if str(room_type) == "Standard":
        num_of_rooms = int(num_of_rooms) * 0.50
    elif str(room_type) == "Queen":
        num_of_rooms = int(num_of_rooms) * 0.30
    elif str(room_type) == "King":
        num_of_rooms = int(num_of_rooms) * 0.20

    cursor = conn.execute("SELECT UID,RID,ROOM_TYPE,START_DATE,END_DATE from RESERVATIONS WHERE HID = '"+str(HID)+"'")

    #traverse through all of reservations.
    conn.commit()
    for row in cursor:
        user_start_date = create_date(str(user_start_date))
        user_end_date = create_date(str(user_end_date))
        reservation_start_date = create_date(row[3])
        reservation_end_date = create_date(row[4])

        #if there is a reservation already conflicting with the time period then decrese the number of rooms
        if str(room_type) == row[2]:
            if not ((user_start_date.date() > reservation_start_date.date() and user_start_date.date() > reservation_end_date.date()) or (user_end_date.date() < reservation_start_date.date() and user_end_date.date() < reservation_end_date.date())):
                num_of_rooms -= 1
                if num_of_rooms == 0:
                    return False
    return True


def does_room_meet_requirements(conn,HID,user_amenities,hotel_amenities,lowest_price,highest_price,user_start_date,user_end_date,num_of_rooms):

    #does the hotel have all of the user requested amenities?
    count = 0
    for amenities in user_amenities:
        if str(amenities) in hotel_amenities:
            count += 1


    #does the hotel have a room that falls between the price range?
    cursor = conn.execute("SELECT HID,NUM,TYPE,PRICE from HOTEL_ROOM")

    conn.commit()

    rooms = {}


    count_price = 0
    for row in cursor:
        if str(HID) == str(row[0]):
            #No user prefereance for price or user amenities
            if user_amenities == [''] and lowest_price == "" and highest_price == "":
                rooms[count_price] = int(row[3])
                count_price +=1
            #user prefereance for price or user amenities
            elif not user_amenities == [''] and not lowest_price == "" and not highest_price == "":
                if (int(row[3]) >= int(lowest_price) and int(row[3]) <= int(highest_price)) and count == len(user_amenities):
                    if is_room_type_available(conn,HID,row[2],num_of_rooms,user_start_date,user_end_date):
                        rooms[count_price] = int(row[3])
                        count_price +=1
            #No user prefereance for amenities but preferance for price
            elif user_amenities == [''] and not lowest_price == "" and not highest_price == "":
                if (int(row[3]) >= int(lowest_price) and int(row[3]) <= int(highest_price)):
                    if is_room_type_available(conn,HID,row[2],num_of_rooms,user_start_date,user_end_date):
                        rooms[count_price] = int(row[3])
                        count_price +=1
            #No user prefereance for price , but preferance for user amenities
            elif not user_amenities == [''] and not lowest_price and not highest_price:
                if count == len(user_amenities):
                    rooms[count_price] = int(row[3])
                    count_price +=1



    if len(rooms) == 0:
        return [False,None]

    else:
        return [True,rooms]




def is_room_available(conn,HID,start_date,end_date,num_of_rooms):
    cursor = conn.execute("SELECT HID,UID,RID,START_DATE,END_DATE from RESERVATIONS")

    #traverse through all of reservations.
    conn.commit()
    for row in cursor:
        if str(HID) == str(row[0]):
            user_start_date = create_date(start_date)
            user_end_date = create_date(end_date)
            reservation_start_date = create_date(row[3])
            reservation_end_date = create_date(row[4])

            #if there is a reservation already conflicting with the time period then decrese the number of rooms
            if not ((user_start_date.date() > reservation_start_date.date() and user_start_date.date() > reservation_end_date.date()) or (user_end_date.date() < reservation_start_date.date() and user_end_date.date() < reservation_end_date.date())):
                num_of_rooms -= 1
                if num_of_rooms == 0:
                    return [False,0]
    return [True,num_of_rooms]



def get_hotel_availability(conn,HID,start_date,end_date,user_amenities,hotel_amenities,lowest_price,highest_price,num_of_rooms):

    rooms_available = is_room_available(conn,HID,start_date,end_date,num_of_rooms)
    requirements = does_room_meet_requirements(conn,HID,user_amenities,hotel_amenities,lowest_price,highest_price,start_date,end_date,num_of_rooms)

    if rooms_available[0] and requirements[0]:
        return [rooms_available[1],requirements[1]]

    return None


def get_hotel_amenities(conn,HID):

    cursor = conn.execute("SELECT HID,TYPE,AVAILABILITY from AMENITIES")

    hotel_amenities = {}

    count = 0
    for row in cursor:

        if str(HID) == str(row[0]):
            hotel_amenities[row[1]] = {"AVAILABILITY" : row[2]}


        count += 1

    conn.commit()

    return hotel_amenities


def user_get_hotels(start_date,end_date,user_amenities,lowest_price,highest_price):
    try:
        print('[!] Accessing Database!')

        conn = sqlite3.connect('/usr/src/app/Backend/Database/test_DB.db')
        cursor = conn.execute("SELECT HID,NAME,NUM_OF_ROOMS,IMG_URL,WEEKEND_PERCENT,PHONE_NUMBER from HOTEL")

        hotels = {}
        count = 0
        for row in cursor:
            hotel_amenities = get_hotel_amenities(conn,row[0])
            hotel_rooms = get_hotel_availability(conn,row[0],start_date,end_date,user_amenities,hotel_amenities,lowest_price,highest_price,row[2])

            if not hotel_rooms == None:
                hotels[count] = {"HID" : row[0], "Name" : row[1], "NUM_OF_ROOMS" : hotel_rooms[0],"WEEKEND_PERCENT":row[4], "PHONE_NUMBER" : row[5], "AMENITIES" : hotel_amenities, "ROOMS": hotel_rooms[1],"IMG_URL":row[3],"OTHER_OFFER":"NO"}
                count += 1


        if count == 0:
            cursor = conn.execute("SELECT HID,NAME,NUM_OF_ROOMS,IMG_URL,WEEKEND_PERCENT,PHONE_NUMBER from HOTEL")

            for row in cursor:
                hotel_amenities = get_hotel_amenities(conn,row[0])
                hotel_rooms = get_hotel_availability(conn,row[0],start_date,end_date,[''],hotel_amenities,"","",row[2])
                if not hotel_rooms == None:
                    hotels[count] = {"HID" : row[0], "Name" : row[1], "NUM_OF_ROOMS" : hotel_rooms[0],"WEEKEND_PERCENT":row[4], "PHONE_NUMBER" : row[5], "AMENITIES" : hotel_amenities, "ROOMS": hotel_rooms[1],"IMG_URL":row[3],"OTHER_OFFER":"YES"}
                    count += 1



        conn.commit()
        conn.close()

        hotels_json = json.dumps(hotels)
        print("[+] Packaged All Hotels into JSON Format")
        return hotels_json
    except:
        conn.close()
