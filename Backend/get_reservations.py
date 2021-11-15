import json
import sqlite3
import datetime
import re




def get_user_reservations(RID,first_name,last_name,email):
    if RID == "" and not first_name == "" and not last_name == "" and not email == "":
        conn = sqlite3.connect('/usr/src/app/Backend/Database/test_DB.db')

        cursor = conn.execute("SELECT HID,UID,RID,ROOM_TYPE,START_DATE,PRICE,EMAIL,FIRST_NAME,LAST_NAME,NUM_ADULTS,NUM_CHILDREN,END_DATE from RESERVATIONS ")



        reservations = {}
        count = 0
        for row in cursor:
            if first_name == str(row[7]) and last_name == str(row[8]) and email == str(row[6]):
                cursor_hotel = conn.execute("SELECT HID,NAME,NUM_OF_ROOMS,IMG_URL,PHONE_NUMBER from HOTEL")
                row_hotel = cursor_hotel.fetchall()
                reservations[count] = {"IMG_URL" : row_hotel[0][3], "Name":row_hotel[0][1], "START_DATE":row[4],"END_DATE":row[11],"ROOM_TYPE":row[3],"Price":row[5],"RID":row[2]}
                count += 1


        conn.commit()
        conn.close()
        print(reservations)
        reservations_json = json.dumps(reservations)
        print("[+] Packaged All Reservations into JSON Format")

        return reservations_json

    elif not RID == "":

        conn = sqlite3.connect('/usr/src/app/Backend/Database/test_DB.db')

        reservations = {}
        cursor = conn.execute("SELECT HID,UID,RID,ROOM_TYPE,START_DATE,PRICE,EMAIL,FIRST_NAME,LAST_NAME,NUM_ADULTS,NUM_CHILDREN,END_DATE from RESERVATIONS WHERE RID ='"+str(RID)+"'")
        row_reservation = cursor.fetchall()

        HID = row_reservation[0][0]
        cursor_hotel = conn.execute("SELECT HID,NAME,NUM_OF_ROOMS,IMG_URL,PHONE_NUMBER from HOTEL WHERE HID ='"+str(HID)+"'")
        row_hotel = cursor_hotel.fetchall()

        reservations[0] = {"IMG_URL" : row_hotel[0][3], "Name":row_hotel[0][1], "START_DATE":row_reservation[0][4],"END_DATE":row_reservation[0][11],"ROOM_TYPE":row_reservation[0][3],"Price":row_reservation[0][5],"RID":row_reservation[0][2]}

        conn.commit()

        conn.close()


        reservations_json = json.dumps(reservations)
        print("[+] Packaged All Reservations into JSON Format")

        return reservations_json
    else:
        return "NO RESERVATIONS"
