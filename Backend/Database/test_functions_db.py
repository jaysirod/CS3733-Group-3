import sqlite3



def print_users():

    conn = sqlite3.connect('test_DB.db')
    cursor = conn.execute("SELECT UID, FIRST_NAME, LAST_NAME, EMAIL, PHONE_NUM from USERS")
    for row in cursor:
        print("UID = ", row[0])
        print("FIRST_NAME = ", row[1])
        print("LAST_NAME = ", row[2])
        print("EMAIL = ", row[3])
        print("PHONE_NUM = ", row[4],"\n")

    conn.commit()
    print("Printed All Users")
    conn.close()




def print_hotels():

    conn = sqlite3.connect('test_DB.db')
    cursor = conn.execute("SELECT HID,NAME,NUM_OF_ROOMS,PHONE_NUMBER from HOTEL")
    for row in cursor:
        print("HID = ", row[0])
        print("NAME = ", row[1])
        print("NUM_OF_ROOMS = ", row[2])
        print("PHONE_NUMBER = ", row[3],"\n")

    conn.commit()
    print("Printed All Hotels")
    conn.close()



def add_users():
    conn = sqlite3.connect('test_DB.db')
    print("Opened database successfully")
    conn.execute("INSERT INTO USERS (UID,FIRST_NAME,LAST_NAME,EMAIL,PHONE_NUM,PASSWORD) \
          VALUES (1000, 'Mario', 'De Jesus', 'test@test.com', 2103075408,'password123')")

    conn.execute("INSERT INTO USERS (UID,FIRST_NAME,LAST_NAME,EMAIL,PHONE_NUM,PASSWORD) \
          VALUES (2000, 'Juan-Carlos', 'Rodriguez', 'test@test.com', 2101234567,'password123')")

    conn.execute("INSERT INTO USERS (UID,FIRST_NAME,LAST_NAME,EMAIL,PHONE_NUM,PASSWORD) \
          VALUES (3000, 'Alan', 'Mendoza', 'test@test.com', 2101234567,'password123')")

    conn.execute("INSERT INTO USERS (UID,FIRST_NAME,LAST_NAME,EMAIL,PHONE_NUM,PASSWORD) \
          VALUES (4000, 'David', 'Jackson', 'test@test.com', 2101234567,'password123')")

    conn.execute("INSERT INTO USERS (UID,FIRST_NAME,LAST_NAME,EMAIL,PHONE_NUM,PASSWORD) \
          VALUES (5000, 'Miguel', 'Alejandro', 'test@test.com', 2101234567,'password123')")


    conn.commit()
    print("Successfully Added Users to Database")
    conn.close()



def add_hotels():
    conn = sqlite3.connect('test_DB.db')
    print("Opened database successfully")
    conn.execute("INSERT INTO HOTEL (HID,NAME,NUM_OF_ROOMS,IMG_URL,PHONE_NUMBER) \
          VALUES (1000, 'The Magnolia All Suites', 20, './hotel_images/hotel_img1.jpg', 2101234567)")

    conn.execute("INSERT INTO HOTEL (HID,NAME,NUM_OF_ROOMS,IMG_URL,PHONE_NUMBER) \
          VALUES (2000, 'The Lofts at Town Centre', 60, './hotel_images/hotel_img2.jpg', 2101234567)")

    conn.execute("INSERT INTO HOTEL (HID,NAME,NUM_OF_ROOMS,IMG_URL,PHONE_NUMBER) \
          VALUES (3000, 'Park North Hotel', 100,'./hotel_images/hotel_img3.jpg', 2101234567)")

    conn.commit()
    print("Successfully Added Hotels to Database")
    conn.close()




def add_anemities():


    conn = sqlite3.connect('test_DB.db')
    print("Opened database successfully")


    conn.execute("INSERT INTO AMENITIES (HID,TYPE,AVAILABILITY) \
          VALUES (1000, 'Pool', 'Open')")

    conn.execute("INSERT INTO AMENITIES (HID,TYPE,AVAILABILITY) \
          VALUES (1000, 'Gym', 'Open')")

    conn.execute("INSERT INTO AMENITIES (HID,TYPE,AVAILABILITY) \
          VALUES (1000, 'Spa', 'Open')")

    conn.execute("INSERT INTO AMENITIES (HID,TYPE,AVAILABILITY) \
          VALUES (1000, 'Business Office', 'Open')")



    conn.execute("INSERT INTO AMENITIES (HID,TYPE,AVAILABILITY) \
          VALUES (2000, 'Pool', 'Open')")

    conn.execute("INSERT INTO AMENITIES (HID,TYPE,AVAILABILITY) \
          VALUES (2000, 'Gym', 'Open')")

    conn.execute("INSERT INTO AMENITIES (HID,TYPE,AVAILABILITY) \
          VALUES (2000, 'Business Office', 'Open')")


    conn.execute("INSERT INTO AMENITIES (HID,TYPE,AVAILABILITY) \
          VALUES (3000, 'Pool', 'Open')")

    conn.execute("INSERT INTO AMENITIES (HID,TYPE,AVAILABILITY) \
          VALUES (3000, 'Gym', 'Open')")


    conn.commit()
    print("Successfully Added Anemities to Database")
    conn.close()



def add_hotel_rooms():
    conn = sqlite3.connect('test_DB.db')
    print("Opened database successfully")


    conn.execute("INSERT INTO HOTEL_ROOM (HID,NUM,TYPE,IMG_URL,PRICE) \
          VALUES (1000, 0,'Standard','./hotel_room_images/hotel_room_img1.jpg', 100)")

    conn.execute("INSERT INTO HOTEL_ROOM (HID,NUM,TYPE,IMG_URL,PRICE) \
          VALUES (1000, 0,'Queen','./hotel_room_images/hotel_room_img2.jpg', 150)")

    conn.execute("INSERT INTO HOTEL_ROOM (HID,NUM,TYPE,IMG_URL,PRICE) \
          VALUES (1000, 0,'King','./hotel_room_images/hotel_room_img3.jpg', 250)")


    conn.execute("INSERT INTO HOTEL_ROOM (HID,NUM,TYPE,IMG_URL,PRICE) \
          VALUES (2000, 0,'Standard','./hotel_room_images/hotel_room_img1.jpg', 105)")

    conn.execute("INSERT INTO HOTEL_ROOM (HID,NUM,TYPE,IMG_URL,PRICE) \
          VALUES (2000, 0,'Queen','./hotel_room_images/hotel_room_img2.jpg', 120)")

    conn.execute("INSERT INTO HOTEL_ROOM (HID,NUM,TYPE,IMG_URL,PRICE) \
          VALUES (2000, 0,'King','./hotel_room_images/hotel_room_img3.jpg', 190)")


    conn.execute("INSERT INTO HOTEL_ROOM (HID,NUM,TYPE,IMG_URL,PRICE) \
          VALUES (3000, 0,'Standard','./hotel_room_images/hotel_room_img1.jpg', 50)")

    conn.execute("INSERT INTO HOTEL_ROOM (HID,NUM,TYPE,IMG_URL,PRICE) \
          VALUES (3000, 0,'Queen','./hotel_room_images/hotel_room_img2.jpg', 75)")

    conn.execute("INSERT INTO HOTEL_ROOM (HID,NUM,TYPE,IMG_URL,PRICE) \
          VALUES (3000, 0,'King','./hotel_room_images/hotel_room_img3.jpg', 90)")


    conn.commit()
    print("Successfully Added Hotel Rooms to Database")
    conn.close()

if __name__ == '__main__':
    add_anemities()
    add_users()
    add_hotels()
    add_hotel_rooms()
