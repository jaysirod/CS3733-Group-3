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


def get_past(UID):
    try:
        conn = sqlite3.connect('/usr/src/app/Backend/Database/test_DB.db')

        reservations = {}
        cursor = conn.execute("SELECT HID,UID,RID,ROOM_TYPE,START_DATE,PRICE,EMAIL,FIRST_NAME,LAST_NAME,NUM_ADULTS,NUM_CHILDREN,END_DATE from RESERVATIONS WHERE UID ='"+str(UID)+"'")
        count = 0
        for row in cursor:
            reservation_date = create_date(row[4])
            if(datetime.datetime.today().date() >= reservation_date.date()):
                HID = row[0]
                cursor_hotel = conn.execute("SELECT HID,NAME,NUM_OF_ROOMS,IMG_URL,PHONE_NUMBER from HOTEL WHERE HID ='"+str(HID)+"'")
                row_hotel = cursor_hotel.fetchall()
                reservations[count] = {"IMG_URL" : row_hotel[0][3], "Name":row_hotel[0][1], "START_DATE":row[4], "END_DATE":row[11],"ROOM_TYPE":row[3],"Price":row[5],"RID":row[2]}
                count +=1




        conn.commit()

        conn.close()


        reservations_json = json.dumps(reservations)
        print("[+] Packaged All Reservations into JSON Format")

        return reservations_json
    except:
        conn.close()


def get_future(UID):
    try:
        conn = sqlite3.connect('/usr/src/app/Backend/Database/test_DB.db')

        reservations = {}
        cursor = conn.execute("SELECT HID,UID,RID,ROOM_TYPE,START_DATE,PRICE,EMAIL,FIRST_NAME,LAST_NAME,NUM_ADULTS,NUM_CHILDREN,END_DATE from RESERVATIONS WHERE UID ='"+str(UID)+"'")
        count = 0
        for row in cursor:
            reservation_date = create_date(row[4])
            if(datetime.datetime.today().date() < reservation_date.date()):
                HID = row[0]
                cursor_hotel = conn.execute("SELECT HID,NAME,NUM_OF_ROOMS,IMG_URL,PHONE_NUMBER from HOTEL WHERE HID ='"+str(HID)+"'")
                row_hotel = cursor_hotel.fetchall()
                reservations[count] = {"IMG_URL" : row_hotel[0][3], "Name":row_hotel[0][1], "START_DATE":row[4], "END_DATE":row[11],"ROOM_TYPE":row[3],"Price":row[5],"RID":row[2]}
                count +=1




        conn.commit()

        conn.close()


        reservations_json = json.dumps(reservations)
        print("[+] Packaged All Reservations into JSON Format")

        return reservations_json
    except:
        conn.close()
