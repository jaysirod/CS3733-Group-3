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


def is_room_type_available(conn,HID,room_type,num_of_rooms,user_start_date,user_end_date,distribution):
    if distribution == 3:
        # out of total num rooms = 50% will be standard , 30% will be Queen, and 20% will be King = 100% total
        if str(room_type) == "Standard":
            num_of_rooms = int(int(num_of_rooms) * 0.50)
        elif str(room_type) == "Queen":
            num_of_rooms = int(int(num_of_rooms) * 0.30)
        elif str(room_type) == "King":
            num_of_rooms = int(int(num_of_rooms) * 0.20)
    elif distribution == 2:
        # 50% split between two rooms
        num_of_rooms = int(int(num_of_rooms) * 0.50)
    elif distribution == 1:
        # one room will contain all of the available rooms 100%
        num_of_rooms = int(int(num_of_rooms) * 1)

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
                    return [False,0]

    return [True, num_of_rooms]





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
    return [True, num_of_rooms]




def get_hotel_amenities(conn,HID):

    cursor = conn.execute("SELECT HID,TYPE,AVAILABILITY from AMENITIES WHERE HID="+str(HID))

    hotel_amenities = {}

    count = 0
    for row in cursor:

        if str(HID) == str(row[0]):
            hotel_amenities[str(row[1])] = {"AVAILABILITY" : row[2]}
            count += 1

    conn.commit()

    return hotel_amenities


def get_hotel_rooms(conn,HID,num_of_rooms,user_start_date,user_end_date):

    cursor = conn.execute("SELECT HID,NUM,TYPE,IMG_URL,PRICE from HOTEL_ROOM WHERE HID="+str(HID))

    hotel_rooms = {}


    #find the available rooms
    count = 0
    rooms_available = []
    for row in cursor:
        if str(row[4]) != "999999":
            rooms_available.append(row)
        else:
            hotel_rooms[str(row[2])] = {'IMAGE_URL':row[3],'PRICE':row[4], 'AVAILABLE': "False","NUM_OF_ROOMS":0}

    rooms_available_distribution = len(rooms_available)

    count = 0
    for row in rooms_available:
        if str(HID) == str(row[0]):
            rooms = is_room_type_available(conn,HID,row[2],num_of_rooms,user_start_date,user_end_date,rooms_available_distribution)
            if rooms[0] == True:
                if str(row[4]) == "999999":
                    hotel_rooms[str(row[2])] = {'IMAGE_URL':row[3],'PRICE':row[4], 'AVAILABLE': "False","NUM_OF_ROOMS":str(rooms[1])}
                else:
                    hotel_rooms[str(row[2])] = {'IMAGE_URL':row[3],'PRICE':row[4] , 'AVAILABLE':"True","NUM_OF_ROOMS":str(rooms[1])}
                count += 1
            else:
                hotel_rooms[str(row[2])] = {'IMAGE_URL':row[3],'PRICE':row[4], 'AVAILABLE': "False","NUM_OF_ROOMS":str(rooms[1])}

    conn.commit()


    return hotel_rooms


def get_hotel_info(HID,start_date,end_date):
    try:
        print('[!] Accessing Database!')

        conn = sqlite3.connect('/usr/src/app/Backend/Database/test_DB.db')

        cursor = conn.execute("SELECT HID,NAME,NUM_OF_ROOMS,IMG_URL,WEEKEND_PERCENT,PHONE_NUMBER from HOTEL WHERE HID="+str(HID))

        row = cursor.fetchall()

        hotel_information = {}

        hotel_amenities = get_hotel_amenities(conn,HID)
        num_of_rooms = row[0][2]
        hotel_rooms = get_hotel_rooms(conn,HID,num_of_rooms,start_date,end_date)

        hotel_information[0] = {"HID" : HID, "Name" : row[0][1], "NUM_OF_ROOMS" : num_of_rooms, "PHONE_NUMBER" : row[0][5], "AMENITIES" : hotel_amenities, "IMG_URL":row[0][3],"WEEKEND_PERCENT":row[0][4],"ROOMS": hotel_rooms}


        conn.commit()
        conn.close()

        hotel_information_json = json.dumps(hotel_information)
        print("[+] Packaged All Of Hotel Information into JSON Format")
        return hotel_information_json
    except:
        conn.close()
