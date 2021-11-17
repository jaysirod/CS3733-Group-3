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


def get_user_reservation(RID):
    try:
        conn = sqlite3.connect('/usr/src/app/Backend/Database/test_DB.db')
        reservations = {}
        count = 0

        cursor = conn.execute("SELECT HID,UID,RID,ROOM_TYPE,START_DATE,PRICE,EMAIL,FIRST_NAME,LAST_NAME,NUM_ADULTS,NUM_CHILDREN,END_DATE from RESERVATIONS WHERE RID ='"+str(RID)+"'")
        row_reservation = cursor.fetchall()

        HID = row_reservation[0][0]
        cursor_hotel = conn.execute("SELECT HID,NAME,NUM_OF_ROOMS,IMG_URL,PHONE_NUMBER from HOTEL WHERE HID ='"+str(HID)+"'")
        row_hotel = cursor_hotel.fetchall()

        cursor_hotel_rooms = conn.execute("SELECT HID,NUM,TYPE,IMG_URL,PRICE from HOTEL_ROOM WHERE HID ='"+str(HID)+"'")

        reservations[0] = {"HName":row_hotel[0][1],"EMAIL" : row_reservation[0][6], "FIRST_NAME":row_reservation[0][7],"LAST_NAME":row_reservation[0][8], "START_DATE":row_reservation[0][4],"NUM_ADULTS":row_reservation[0][9],"NUM_CHILDREN":row_reservation[0][10],"END_DATE":row_reservation[0][11],"ROOM_TYPE":row_reservation[0][3],"Price":row_reservation[0][5],"RID":row_reservation[0][2],"Standard":{},"Queen":{},"King":{}}



        #find the available rooms
        count = 0
        rooms_available = []
        for row in cursor_hotel_rooms:
            if str(row[4]) != "999999":
                rooms_available.append(row)
            else:
                reservations[0][str(row[2])] = {'IMG_URL':row[3],'PRICE':row[4], 'AVAILABLE': "False","NUM":0}

        rooms_available_distribution = len(rooms_available)

        count = 0
        for row in rooms_available:
            if str(HID) == str(row[0]):
                rooms = is_room_type_available(conn,HID,row[2],row_hotel[0][2],row_reservation[0][4],row_reservation[0][11],rooms_available_distribution)
                if rooms[0] == True:
                    if str(row[4]) == "999999":
                        reservations[0][str(row[2])] = {'IMG_URL':row[3],'PRICE':row[4], 'AVAILABLE': "False","NUM":str(rooms[1])}
                    else:
                        reservations[0][str(row[2])] = {'IMG_URL':row[3],'PRICE':row[4] , 'AVAILABLE':"True","NUM":str(rooms[1])}
                    count += 1
                else:
                    reservations[0][str(row[2])] = {'IMG_URL':row[3],'PRICE':row[4], 'AVAILABLE': "False","NUM":str(rooms[1])}

        conn.commit()
        conn.close()


        reservations_json = json.dumps(reservations)
        print("[+] Packaged All Reservations into JSON Format")

        return reservations_json
    except:
        conn.close()
