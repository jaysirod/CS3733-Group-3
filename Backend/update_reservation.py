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

    if str(room_type) == "Standard":
        num_of_rooms = int(num_of_rooms) * 0.50
    elif str(room_type) == "Queen":
        num_of_rooms = int(num_of_rooms) * 0.30
    elif str(room_type) == "King":
        num_of_rooms = int(num_of_rooms) * 0.20

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
                    return False
    return True


def update_user_reservation(RID,user_email,first_name,last_name,room_type,start_date,end_date,adult_num,children_num):
    conn = sqlite3.connect('./Database/test_DB.db')

    cursor = conn.execute("SELECT HID,UID,RID,ROOM_TYPE,START_DATE,PRICE,EMAIL,FIRST_NAME,LAST_NAME,NUM_ADULTS,NUM_CHILDREN,END_DATE from RESERVATIONS WHERE RID ='"+str(RID)+"'")
    row_reservation = cursor.fetchall()

    HID = row_reservation[0][0]
    cursor_hotel = conn.execute("SELECT HID,NAME,NUM_OF_ROOMS,IMG_URL,PHONE_NUMBER from HOTEL WHERE HID ='"+str(HID)+"'")
    row_hotel = cursor_hotel.fetchall()

    cursor_hotel_rooms = conn.execute("SELECT HID,NUM,TYPE,IMG_URL,PRICE from HOTEL_ROOM WHERE HID ='"+str(HID)+"' AND TYPE = '"+str(room_type)+"'")
    row_hotel_rooms = cursor_hotel_rooms.fetchall()


    price = str(round(float((int(row_hotel_rooms[0][4]) * 0.0825) + int(row_hotel_rooms[0][4])), 2))
    if is_room_available(conn,HID,start_date,end_date,int(row_hotel[0][2]),room_type):
        conn.execute("UPDATE RESERVATIONS SET ROOM_TYPE = '"+room_type+"',START_DATE = '"+start_date+"',PRICE = '"+str(price)+"',EMAIL = '"+user_email+"',FIRST_NAME = '"+first_name+"',LAST_NAME = '"+last_name+"',NUM_ADULTS = '"+adult_num+"',NUM_CHILDREN = '"+children_num+"',END_DATE = '"+end_date+"' WHERE RID='"+str(RID)+"'")
        conn.commit()
        conn.close()
        print("[+] Successfully Updated Reservation")

        return "0"
    else:
        conn.close()
        print("[+] Failed to Update Reservation")

        return "1"
