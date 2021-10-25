import json
import sqlite3
import datetime
import re


def create(HID,UID,RID,start_date,end_date,ROOM_TYPE,price,num_adult,num_children,first_name,last_name,user_email):

    # Make sure the hotel is still available

    print('[!] Accessing Database!')

    conn = sqlite3.connect('./Database/test_DB.db')


    conn.execute("INSERT INTO RESERVATIONS (HID,UID,RID,ROOM_TYPE,START_DATE,PRICE,EMAIL,FIRST_NAME,LAST_NAME,NUM_ADULTS,NUM_CHILDREN,END_DATE) \
          VALUES ('"+HID+"', '"+UID+"', '"+RID+"', '"+ROOM_TYPE+"','"+start_date+"', '"+price+"','"+user_email+"','"+first_name+"','"+last_name+"','"+num_adult+"','"+num_children+"','"+end_date+"')")

    conn.commit()
    conn.close()
    print('[+] Reservation Created')
    return "0"
