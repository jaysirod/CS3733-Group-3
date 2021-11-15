import json
import sqlite3
import datetime
import re

def add_amenities(HID,amenities,amenities_availability):
    try:
        conn = sqlite3.connect('/usr/src/app/Backend/Database/test_DB.db')


        for i in range(len(amenities)-1):
            conn.execute("INSERT INTO AMENITIES (HID,TYPE,AVAILABILITY) \
                  VALUES ('"+HID+"', '"+amenities[i]+"', '"+amenities_availability[i]+"')")
            conn.commit()

        conn.close()
    except:
        conn.close()



def add_rooms(HID,standard_image,standard_price,queen_image,queen_price,king_image,king_price):
    try:
        conn = sqlite3.connect('/usr/src/app/Backend/Database/test_DB.db')

        conn.execute("INSERT INTO HOTEL_ROOM (HID,NUM,TYPE,IMG_URL,PRICE) \
              VALUES ('"+str(HID)+"', 0,'Standard','hotel_room_images/"+standard_image+"', '"+standard_price+"')")
        conn.commit()

        conn.execute("INSERT INTO HOTEL_ROOM (HID,NUM,TYPE,IMG_URL,PRICE) \
              VALUES ('"+str(HID)+"', 0,'Queen','hotel_room_images/"+queen_image+"', '"+queen_price+"')")
        conn.commit()

        conn.execute("INSERT INTO HOTEL_ROOM (HID,NUM,TYPE,IMG_URL,PRICE) \
              VALUES ('"+str(HID)+"', 0,'King','hotel_room_images/"+king_image+"', '"+king_price+"')")
        conn.commit()
        conn.close()
    except:
        conn.close()


def add_hotel(HID,hotel_name,num_of_rooms,hotel_img,weekend_percent,phone_number,standard_image,standard_price,queen_image,queen_price,king_image,king_price,amenities,amenities_availability):
    try:
        print('[!] Accessing Database!')


        conn = sqlite3.connect('/usr/src/app/Backend/Database/test_DB.db')

        conn.execute("INSERT INTO HOTEL (HID,NAME,NUM_OF_ROOMS,IMG_URL,WEEKEND_PERCENT,PHONE_NUMBER) \
              VALUES ('"+str(HID)+"', '"+hotel_name+"', '"+num_of_rooms+"','hotel_images/"+hotel_img+"','"+weekend_percent+"', '"+phone_number+"')")

        conn.commit()
        add_rooms(HID,standard_image,standard_price,queen_image,queen_price,king_image,king_price)
        add_amenities(HID,amenities,amenities_availability)


        conn.close()

        print('[!] Successfully Added Hotel')
        return "0"
    except:
        conn.close()
