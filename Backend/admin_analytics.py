import json
import sqlite3
import datetime
import re
from datetime import timedelta
def find_max_room(rooms):
    max_room = 0
    max_index = 0
    for i in range(len(rooms)):
        if max_room < int(rooms[i]):
            max_room = int(rooms[i])
            max_index = i

    if max_room == 0:
        return "None"
    if max_index == 0:
        return "Standard"
    elif max_index == 1:
        return "Queen"
    elif max_index == 2:
        return "King"



def get_reservations(time_period,hotel_id):
    if time_period == "Today":
        conn = sqlite3.connect('./Database/test_DB.db')

        if hotel_id == "All Hotels":
            cursor = conn.execute("SELECT HID,UID,RID,ROOM_TYPE,START_DATE,PRICE,NUM_ADULTS,NUM_CHILDREN,END_DATE from RESERVATIONS ")
        else:
            cursor = conn.execute("SELECT HID,UID,RID,ROOM_TYPE,START_DATE,PRICE,NUM_ADULTS,NUM_CHILDREN,END_DATE from RESERVATIONS WHERE HID='"+str(hotel_id)+"'")


        reservations = {}
        count = 0
        total_revenue = 0
        total_bookings = 0
        popular_room = [0,0,0]

        for row in cursor:
            processed_date = re.search(r'([0-9]*)-([0-9]*)-([0-9]*)', str(row[4]))

            month = int(processed_date.group(2))
            day = int(processed_date.group(3))
            year = int(processed_date.group(1))

            if datetime.datetime(year,month,day).date() == datetime.datetime.today().date():
                reservations[count] = {"HID" : row[0], "UID" : row[1],"RID" : row[2],"ROOM_TYPE" : row[3],"START_DATE" : row[4],"PRICE" : row[5],"NUM_ADULTS" : row[6],"NUM_CHILDREN" : row[7],"END_DATE" : row[8]}
                count += 1
                total_revenue += int(row[5])
                if row[3] == "Standard":
                    popular_room[0] += 1
                elif row[3] == "Queen":
                    popular_room[1] += 1
                elif row[3] == "King":
                    popular_room[2] += 1


        total_bookings = count
        popular_room = find_max_room(popular_room)

        reservations[count] = {"Revenue":total_revenue,"Bookings":total_bookings,"Popular_Room":popular_room}
        conn.commit()
        conn.close()

        reservations_json = json.dumps(reservations)
        print("[+] Packaged All Reservations into JSON Format")
        return reservations_json


    elif time_period == "Yesterday":
        conn = sqlite3.connect('./Database/test_DB.db')

        if hotel_id == "All Hotels":
            cursor = conn.execute("SELECT HID,UID,RID,ROOM_TYPE,START_DATE,PRICE,NUM_ADULTS,NUM_CHILDREN,END_DATE from RESERVATIONS ")
        else:
            cursor = conn.execute("SELECT HID,UID,RID,ROOM_TYPE,START_DATE,PRICE,NUM_ADULTS,NUM_CHILDREN,END_DATE from RESERVATIONS WHERE HID='"+str(hotel_id)+"'")


        reservations = {}
        count = 0
        total_revenue = 0
        total_bookings = 0
        popular_room = [0,0,0]

        for row in cursor:
            processed_date = re.search(r'([0-9]*)-([0-9]*)-([0-9]*)', str(row[4]))

            month = int(processed_date.group(2))
            day = int(processed_date.group(3))
            year = int(processed_date.group(1))

            if datetime.datetime(year,month,day).date() == (datetime.datetime.now() - timedelta(1)).date():
                reservations[count] = {"HID" : row[0], "UID" : row[1],"RID" : row[2],"ROOM_TYPE" : row[3],"START_DATE" : row[4],"PRICE" : row[5],"NUM_ADULTS" : row[6],"NUM_CHILDREN" : row[7],"END_DATE" : row[8]}
                count += 1
                total_revenue += int(row[5])
                if row[3] == "Standard":
                    popular_room[0] += 1
                elif row[3] == "Queen":
                    popular_room[1] += 1
                elif row[3] == "King":
                    popular_room[2] += 1


        total_bookings = count
        popular_room = find_max_room(popular_room)

        reservations[count] = {"Revenue":total_revenue,"Bookings":total_bookings,"Popular_Room":popular_room}
        conn.commit()
        conn.close()

        reservations_json = json.dumps(reservations)
        print("[+] Packaged All Reservations into JSON Format")
        return reservations_json

    elif time_period == "Past 7 Days":
        conn = sqlite3.connect('./Database/test_DB.db')

        if hotel_id == "All Hotels":
            cursor = conn.execute("SELECT HID,UID,RID,ROOM_TYPE,START_DATE,PRICE,NUM_ADULTS,NUM_CHILDREN,END_DATE from RESERVATIONS ")
        else:
            cursor = conn.execute("SELECT HID,UID,RID,ROOM_TYPE,START_DATE,PRICE,NUM_ADULTS,NUM_CHILDREN,END_DATE from RESERVATIONS WHERE HID='"+str(hotel_id)+"'")


        reservations = {}
        count = 0
        total_revenue = 0
        total_bookings = 0
        popular_room = [0,0,0]

        for row in cursor:
            processed_date = re.search(r'([0-9]*)-([0-9]*)-([0-9]*)', str(row[4]))

            month = int(processed_date.group(2))
            day = int(processed_date.group(3))
            year = int(processed_date.group(1))

            if datetime.datetime(year,month,day).date() >= (datetime.datetime.now() - timedelta(7)).date() and datetime.datetime(year,month,day).date() < datetime.datetime.today().date():
                reservations[count] = {"HID" : row[0], "UID" : row[1],"RID" : row[2],"ROOM_TYPE" : row[3],"START_DATE" : row[4],"PRICE" : row[5],"NUM_ADULTS" : row[6],"NUM_CHILDREN" : row[7],"END_DATE" : row[8]}
                count += 1
                total_revenue += int(row[5])
                if row[3] == "Standard":
                    popular_room[0] += 1
                elif row[3] == "Queen":
                    popular_room[1] += 1
                elif row[3] == "King":
                    popular_room[2] += 1


        total_bookings = count
        popular_room = find_max_room(popular_room)

        reservations[count] = {"Revenue":total_revenue,"Bookings":total_bookings,"Popular_Room":popular_room}
        conn.commit()
        conn.close()

        reservations_json = json.dumps(reservations)
        print("[+] Packaged All Reservations into JSON Format")
        return reservations_json


    elif time_period == "Past 30 Days":
        conn = sqlite3.connect('./Database/test_DB.db')

        if hotel_id == "All Hotels":
            cursor = conn.execute("SELECT HID,UID,RID,ROOM_TYPE,START_DATE,PRICE,NUM_ADULTS,NUM_CHILDREN,END_DATE from RESERVATIONS ")
        else:
            cursor = conn.execute("SELECT HID,UID,RID,ROOM_TYPE,START_DATE,PRICE,NUM_ADULTS,NUM_CHILDREN,END_DATE from RESERVATIONS WHERE HID='"+str(hotel_id)+"'")


        reservations = {}
        count = 0
        total_revenue = 0
        total_bookings = 0
        popular_room = [0,0,0]

        for row in cursor:
            processed_date = re.search(r'([0-9]*)-([0-9]*)-([0-9]*)', str(row[4]))

            month = int(processed_date.group(2))
            day = int(processed_date.group(3))
            year = int(processed_date.group(1))

            if datetime.datetime(year,month,day).date() >= (datetime.datetime.now() - timedelta(30)).date() and datetime.datetime(year,month,day).date() < datetime.datetime.today().date():
                reservations[count] = {"HID" : row[0], "UID" : row[1],"RID" : row[2],"ROOM_TYPE" : row[3],"START_DATE" : row[4],"PRICE" : row[5],"NUM_ADULTS" : row[6],"NUM_CHILDREN" : row[7],"END_DATE" : row[8]}
                count += 1
                total_revenue += int(row[5])
                if row[3] == "Standard":
                    popular_room[0] += 1
                elif row[3] == "Queen":
                    popular_room[1] += 1
                elif row[3] == "King":
                    popular_room[2] += 1


        total_bookings = count
        popular_room = find_max_room(popular_room)

        reservations[count] = {"Revenue":total_revenue,"Bookings":total_bookings,"Popular_Room":popular_room}
        conn.commit()
        conn.close()

        reservations_json = json.dumps(reservations)
        print("[+] Packaged All Reservations into JSON Format")
        return reservations_json


    elif time_period == "Past 365 Days":
        conn = sqlite3.connect('./Database/test_DB.db')

        if hotel_id == "All Hotels":
            cursor = conn.execute("SELECT HID,UID,RID,ROOM_TYPE,START_DATE,PRICE,NUM_ADULTS,NUM_CHILDREN,END_DATE from RESERVATIONS ")
        else:
            cursor = conn.execute("SELECT HID,UID,RID,ROOM_TYPE,START_DATE,PRICE,NUM_ADULTS,NUM_CHILDREN,END_DATE from RESERVATIONS WHERE HID='"+str(hotel_id)+"'")


        reservations = {}
        count = 0
        total_revenue = 0
        total_bookings = 0
        popular_room = [0,0,0]

        for row in cursor:
            processed_date = re.search(r'([0-9]*)-([0-9]*)-([0-9]*)', str(row[4]))

            month = int(processed_date.group(2))
            day = int(processed_date.group(3))
            year = int(processed_date.group(1))

            if datetime.datetime(year,month,day).date() >= (datetime.datetime.now() - timedelta(365)).date() and datetime.datetime(year,month,day).date() < datetime.datetime.today().date():
                reservations[count] = {"HID" : row[0], "UID" : row[1],"RID" : row[2],"ROOM_TYPE" : row[3],"START_DATE" : row[4],"PRICE" : row[5],"NUM_ADULTS" : row[6],"NUM_CHILDREN" : row[7],"END_DATE" : row[8]}
                count += 1
                total_revenue += int(row[5])
                if row[3] == "Standard":
                    popular_room[0] += 1
                elif row[3] == "Queen":
                    popular_room[1] += 1
                elif row[3] == "King":
                    popular_room[2] += 1


        total_bookings = count
        popular_room = find_max_room(popular_room)

        reservations[count] = {"Revenue":total_revenue,"Bookings":total_bookings,"Popular_Room":popular_room}
        conn.commit()
        conn.close()

        reservations_json = json.dumps(reservations)
        print("[+] Packaged All Reservations into JSON Format")
        return reservations_json


    elif time_period == "All Time":

        conn = sqlite3.connect('./Database/test_DB.db')
        if hotel_id == "All Hotels":
            cursor = conn.execute("SELECT HID,UID,RID,ROOM_TYPE,START_DATE,PRICE,NUM_ADULTS,NUM_CHILDREN,END_DATE from RESERVATIONS ")
        else:
            cursor = conn.execute("SELECT HID,UID,RID,ROOM_TYPE,START_DATE,PRICE,NUM_ADULTS,NUM_CHILDREN,END_DATE from RESERVATIONS WHERE HID='"+str(hotel_id)+"'")

        reservations = {}
        count = 0

        total_revenue = 0
        total_bookings = 0
        popular_room = [0,0,0]

        for row in cursor:
            reservations[count] = {"HID" : row[0], "UID" : row[1],"RID" : row[2],"ROOM_TYPE" : row[3],"START_DATE" : row[4],"PRICE" : row[5],"NUM_ADULTS" : row[6],"NUM_CHILDREN" : row[7],"END_DATE" : row[8]}
            count += 1
            total_revenue += int(row[5])
            if row[3] == "Standard":
                popular_room[0] += 1
            elif row[3] == "Queen":
                popular_room[1] += 1
            elif row[3] == "King":
                popular_room[2] += 1


        total_bookings = count
        popular_room = find_max_room(popular_room)

        reservations[count] = {"Revenue":total_revenue,"Bookings":total_bookings,"Popular_Room":popular_room}
        conn.commit()
        conn.close()

        reservations_json = json.dumps(reservations)
        print("[+] Packaged All Reservations into JSON Format")
        return reservations_json
