import json
import sqlite3
import datetime
import re


def update_amenities(HID,amenities,amenities_availability):
    conn = sqlite3.connect('/usr/src/app/Backend/Database/test_DB.db')


    conn.execute("DELETE FROM AMENITIES WHERE HID="+str(HID))
    conn.commit()

    for i in range(len(amenities)-1):
        conn.execute("INSERT INTO AMENITIES (HID,TYPE,AVAILABILITY) \
              VALUES ('"+HID+"', '"+amenities[i]+"', '"+amenities_availability[i]+"')")
        conn.commit()

    conn.close()



def update_rooms(HID,standard_image,standard_price,queen_image,queen_price,king_image,king_price):
    conn = sqlite3.connect('/usr/src/app/Backend/Database/test_DB.db')


    if not standard_image:
        cursor = conn.execute("UPDATE HOTEL_ROOM SET PRICE = '"+standard_price+"' WHERE HID='"+str(HID)+"' AND TYPE = 'Standard'")
    else:
        cursor = conn.execute("UPDATE HOTEL_ROOM SET IMG_URL = 'hotel_room_images/"+standard_image+"', PRICE = '"+standard_price+"' WHERE HID='"+str(HID)+"' AND TYPE = 'Standard'")

    conn.commit()
    if not queen_image:
        cursor = conn.execute("UPDATE HOTEL_ROOM SET PRICE = '"+queen_price+"' WHERE HID='"+str(HID)+"' AND TYPE = 'Queen'")
    else:
        cursor = conn.execute("UPDATE HOTEL_ROOM SET IMG_URL = 'hotel_room_images/"+queen_image+"', PRICE = '"+queen_price+"' WHERE HID='"+str(HID)+"' AND TYPE = 'Queen'")

    conn.commit()
    if not king_image:
        cursor = conn.execute("UPDATE HOTEL_ROOM SET PRICE = '"+king_price+"' WHERE HID='"+str(HID)+"'AND TYPE = 'King'")
    else:
        cursor = conn.execute("UPDATE HOTEL_ROOM SET IMG_URL = 'hotel_room_images/"+king_image+"', PRICE = '"+king_price+"' WHERE HID='"+str(HID)+"' AND TYPE = 'King'")
    conn.commit()
    conn.close()


def update_hotel(HID,hotel_name,num_of_rooms,hotel_img,weekend_percent,phone_number,standard_image,standard_price,queen_image,queen_price,king_image,king_price,amenities,amenities_availability):
    print('[!] Accessing Database!')


    conn = sqlite3.connect('/usr/src/app/Backend/Database/test_DB.db')

    print(hotel_name)

    if not hotel_img:
        cursor = conn.execute("UPDATE HOTEL SET NAME = '"+hotel_name+"', NUM_OF_ROOMS = '"+num_of_rooms+"',PHONE_NUMBER='"+phone_number+"' ,WEEKEND_PERCENT='"+weekend_percent+"' WHERE HID="+str(HID))
    else:
        cursor = conn.execute("UPDATE HOTEL SET NAME = '"+hotel_name+"', NUM_OF_ROOMS = '"+num_of_rooms+"', IMG_URL = 'hotel_images/"+hotel_img+"',PHONE_NUMBER='"+phone_number+"' ,WEEKEND_PERCENT='"+weekend_percent+"' WHERE HID="+str(HID))

    conn.commit()
    update_rooms(HID,standard_image,standard_price,queen_image,queen_price,king_image,king_price)
    update_amenities(HID,amenities,amenities_availability)


    conn.close()

    print('[!] Successfully Finished Hotel Update')
    return "0"
