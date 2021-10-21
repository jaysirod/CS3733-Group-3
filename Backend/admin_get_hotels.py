import json
import sqlite3
import datetime
import re

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


def get_hotels_admin():
    print('[!] Accessing Database!')

    conn = sqlite3.connect('./Database/test_DB.db')
    cursor = conn.execute("SELECT HID,NAME,NUM_OF_ROOMS,IMG_URL,PHONE_NUMBER from HOTEL")

    hotels = {}
    count = 0
    for row in cursor:

        hotel_amenities = get_hotel_amenities(conn,row[0])

        hotels[count] = {"HID" : row[0], "Name" : row[1], "PHONE_NUMBER" : row[4], "AMENITIES" : hotel_amenities, "IMG_URL" : row[3]}
        count += 1


    conn.commit()
    conn.close()

    hotels_json = json.dumps(hotels)
    print("[+] Packaged All Hotels into JSON Format")
    return hotels_json
