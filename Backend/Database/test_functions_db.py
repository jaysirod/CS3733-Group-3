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
    conn.execute("INSERT INTO USERS (UID,ADMIN,FIRST_NAME,LAST_NAME,EMAIL,PHONE_NUM,PASSWORD) \
          VALUES (1000, 1, 'Mario', 'De Jesus', 'test@test.com', 2103075408,'password123')")

    conn.execute("INSERT INTO USERS (UID,ADMIN,FIRST_NAME,LAST_NAME,EMAIL,PHONE_NUM,PASSWORD) \
          VALUES (2000, 1, 'Juan-Carlos', 'Rodriguez', 'test@test.com', 2101234567,'password123')")

    conn.execute("INSERT INTO USERS (UID,ADMIN,FIRST_NAME,LAST_NAME,EMAIL,PHONE_NUM,PASSWORD) \
          VALUES (3000, 1, 'Alan', 'Mendoza', 'test@test.com', 2101234567,'password123')")

    conn.execute("INSERT INTO USERS (UID,ADMIN,FIRST_NAME,LAST_NAME,EMAIL,PHONE_NUM,PASSWORD) \
          VALUES (4000, 1, 'David', 'Jackson', 'test@test.com', 2101234567,'password123')")

    conn.execute("INSERT INTO USERS (UID,ADMIN,FIRST_NAME,LAST_NAME,EMAIL,PHONE_NUM,PASSWORD) \
          VALUES (5000, 1, 'Miguel', 'Alejandro', 'test@test.com', 2101234567,'password123')")


    conn.commit()
    print("Successfully Added Users to Database")
    conn.close()



def add_hotels():
    conn = sqlite3.connect('test_DB.db')
    print("Opened database successfully")
    conn.execute("INSERT INTO HOTEL (HID,NAME,NUM_OF_ROOMS,PHONE_NUMBER) \
          VALUES (1000, 'The Magnolia All Suites', 20, 2101234567)")

    conn.execute("INSERT INTO HOTEL (HID,NAME,NUM_OF_ROOMS,PHONE_NUMBER) \
          VALUES (2000, 'The Lofts at Town Centre', 60, 2101234567)")

    conn.execute("INSERT INTO HOTEL (HID,NAME,NUM_OF_ROOMS,PHONE_NUMBER) \
          VALUES (3000, 'Park North Hotel', 100, 2101234567)")

    conn.commit()
    print("Successfully Added Hotels to Database")
    conn.close()



if __name__ == '__main__':
    print_hotels()
