import json
import sqlite3
import datetime
import re




def delete_hotel(HID):
    conn = sqlite3.connect('/usr/src/app/Backend/Database/test_DB.db')


    conn.execute("DELETE FROM HOTEL WHERE HID='"+str(HID)+"'")
    conn.commit()
    conn.execute("DELETE FROM HOTEL_ROOM WHERE HID='"+str(HID)+"'")
    conn.commit()
    conn.execute("DELETE FROM AMENITIES WHERE HID='"+str(HID)+"'")
    conn.commit()
    conn.execute("DELETE FROM RESERVATIONS WHERE HID='"+str(HID)+"'")
    conn.commit()
    conn.close()

    return "0"
