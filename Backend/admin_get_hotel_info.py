import json
import sqlite3
import datetime
import re



def get_hotel_amenities(conn,HID):

    cursor = conn.execute("SELECT HID,TYPE,AVAILABILITY from AMENITIES WHERE HID="+str(HID))

    hotel_amenities = {}

    count = 0
    for row in cursor:

        if str(HID) == str(row[0]):
            hotel_amenities[count] = {"TYPE":row[1],"AVAILABILITY" : row[2]}
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


def get_hotel_info(HID):
    print('[!] Accessing Database!')

    conn = sqlite3.connect('/usr/src/app/Backend/Database/test_DB.db')

    cursor = conn.execute("SELECT HID,NAME,NUM_OF_ROOMS,IMG_URL,WEEKEND_PERCENT,PHONE_NUMBER from HOTEL WHERE HID="+str(HID))

    row = cursor.fetchall()

    hotel_information = {}

    hotel_amenities = get_hotel_amenities(conn,HID)
    hotel_rooms = get_hotel_rooms(conn,HID)

    hotel_information[0] = {"HID" : HID, "Name" : row[0][1], "NUM_OF_ROOMS" : row[0][2],"WEEKEND_PERCENT":row[0][4], "PHONE_NUMBER" : row[0][5], "AMENITIES" : hotel_amenities, "IMG_URL":row[0][3],"ROOMS": hotel_rooms}


    conn.commit()
    conn.close()

    hotel_information_json = json.dumps(hotel_information)
    print("[+] Packaged All Of Hotel Information into JSON Format")
    return hotel_information_json
