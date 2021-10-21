import json
import sqlite3
import datetime
import re


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
            if not ((reservation_start_date < user_start_date and reservation_end_date < user_start_date) or (reservation_end_date > user_end_date and reservation_start_date > user_end_date)):
                num_of_rooms -= 1
                if num_of_rooms == 0:
                    return [False,0]
    return num_of_rooms




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


def get_hotel_rooms(conn,HID):

    cursor = conn.execute("SELECT HID,NUM,TYPE,IMG_URL,PRICE from HOTEL_ROOM WHERE HID="+str(HID))

    hotel_rooms = {}

    count = 0
    for row in cursor:
        if str(HID) == str(row[0]):
            hotel_rooms[str(row[2])] = {'IMAGE_URL':row[3],'PRICE':row[4]}
            count += 1

    conn.commit()

    return hotel_rooms


def get_hotel_info(HID,start_date,end_date):
    print('[!] Accessing Database!')

    conn = sqlite3.connect('./Database/test_DB.db')

    cursor = conn.execute("SELECT HID,NAME,NUM_OF_ROOMS,IMG_URL,PHONE_NUMBER from HOTEL WHERE HID="+str(HID))

    row = cursor.fetchall()

    hotel_information = {}

    hotel_amenities = get_hotel_amenities(conn,HID)
    hotel_rooms = get_hotel_rooms(conn,HID)
    num_of_rooms = is_room_available(conn,HID,start_date,end_date,row[0][2])

    hotel_information[0] = {"HID" : HID, "Name" : row[0][1], "NUM_OF_ROOMS" : num_of_rooms, "PHONE_NUMBER" : row[0][4], "AMENITIES" : hotel_amenities, "IMG_URL":row[0][3],"ROOMS": hotel_rooms}


    conn.commit()
    conn.close()

    hotel_information_json = json.dumps(hotel_information)
    print("[+] Packaged All Of Hotel Information into JSON Format")
    return hotel_information_json
