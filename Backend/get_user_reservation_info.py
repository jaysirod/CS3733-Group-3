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


def is_room_available(conn,HID,start_date,end_date,num_of_rooms,room_type):
    cursor = conn.execute("SELECT HID,UID,RID,ROOM_TYPE,START_DATE,END_DATE from RESERVATIONS")

    #traverse through all of reservations.
    conn.commit()
    for row in cursor:
        if str(HID) == str(row[0]) and str(room_type) == str(row[3]):
            user_start_date = create_date(start_date)
            user_end_date = create_date(end_date)
            reservation_start_date = create_date(row[4])
            reservation_end_date = create_date(row[5])

            #if there is a reservation already conflicting with the time period then decrese the number of rooms
            if not ((user_start_date.date() > reservation_start_date.date() and user_start_date.date() > reservation_end_date.date()) or (user_end_date.date() < reservation_start_date.date() and user_end_date.date() < reservation_end_date.date())):
                num_of_rooms -= 1
                if num_of_rooms == 0:
                    return 0
    return num_of_rooms


def get_user_reservation(RID):

    conn = sqlite3.connect('./Database/test_DB.db')
    reservations = {}
    count = 0

    cursor = conn.execute("SELECT HID,UID,RID,ROOM_TYPE,START_DATE,PRICE,EMAIL,FIRST_NAME,LAST_NAME,NUM_ADULTS,NUM_CHILDREN,END_DATE from RESERVATIONS WHERE RID ='"+str(RID)+"'")
    row_reservation = cursor.fetchall()

    HID = row_reservation[0][0]
    cursor_hotel = conn.execute("SELECT HID,NAME,NUM_OF_ROOMS,IMG_URL,PHONE_NUMBER from HOTEL WHERE HID ='"+str(HID)+"'")
    row_hotel = cursor_hotel.fetchall()

    cursor_hotel_rooms = conn.execute("SELECT HID,NUM,TYPE,IMG_URL,PRICE from HOTEL_ROOM WHERE HID ='"+str(HID)+"'")

    reservations[0] = {"HName":row_hotel[0][1],"EMAIL" : row_reservation[0][6], "FIRST_NAME":row_reservation[0][7],"LAST_NAME":row_reservation[0][8], "START_DATE":row_reservation[0][4],"NUM_ADULTS":row_reservation[0][9],"NUM_CHILDREN":row_reservation[0][10],"END_DATE":row_reservation[0][11],"ROOM_TYPE":row_reservation[0][3],"Price":row_reservation[0][5],"RID":row_reservation[0][2],"Standard":{},"Queen":{},"King":{}}

    for row_room in cursor_hotel_rooms:
        if row_room[2] == "Standard":
            num_rooms = is_room_available(conn, HID, row_reservation[0][4],row_reservation[0][11],int(int(row_hotel[0][2]) * 0.50),"Standard")
            if num_rooms > 0:
                reservations[0]["Standard"] = {"NUM":num_rooms,"IMG_URL":row_room[3],"PRICE":row_room[4],"AVAILABLE":"True"}
            else:
                reservations[0]["Standard"] = {"NUM":num_rooms,"IMG_URL":row_room[3],"PRICE":row_room[4],"AVAILABLE":"False"}

        elif row_room[2] == "Queen":
            num_rooms = is_room_available(conn, HID, row_reservation[0][4],row_reservation[0][11],int(int(row_hotel[0][2]) * 0.30),"Queen")
            if num_rooms > 0:
                reservations[0]["Queen"] = {"NUM":num_rooms,"IMG_URL":row_room[3],"PRICE":row_room[4],"AVAILABLE":"True"}
            else:
                reservations[0]["Queen"] = {"NUM":num_rooms,"IMG_URL":row_room[3],"PRICE":row_room[4],"AVAILABLE":"False"}
        elif row_room[2] == "King":
            num_rooms = is_room_available(conn, HID, row_reservation[0][4],row_reservation[0][11],int(int(row_hotel[0][2]) * 0.20),"King")
            if num_rooms > 0:
                reservations[0]["King"] = {"NUM":num_rooms,"IMG_URL":row_room[3],"PRICE":row_room[4],"AVAILABLE":"True"}
            else:
                reservations[0]["King"] = {"NUM":num_rooms,"IMG_URL":row_room[3],"PRICE":row_room[4],"AVAILABLE":"False"}


    conn.commit()

    conn.close()


    reservations_json = json.dumps(reservations)
    print("[+] Packaged All Reservations into JSON Format")

    return reservations_json
