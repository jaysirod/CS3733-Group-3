import json
import sqlite3



def user_get_hotels(date_range,anemities,price):
    print('[!] Accessing Database!')

    conn = sqlite3.connect('./Database/test_DB.db')
    cursor = conn.execute("SELECT HID,NAME,NUM_OF_ROOMS,PHONE_NUMBER from HOTEL")

    hotels = {}

    count = 0
    for row in cursor:

        hotels[count] = {"HID" : row[0], "Name" : row[1], "NUM_OF_ROOMS" : row[2], "PHONE_NUMBER" : row[3]}

        count += 1
        
    conn.commit()
    conn.close()

    hotels_json = json.dumps(hotels)
    print("[+] Packaged All Hotels into JSON Format")
    return hotels_json
