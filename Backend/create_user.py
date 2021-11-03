import json
import sqlite3
import datetime
import re




def create_user(UID,first_name,last_name,user_email,phone_number,password):

    print('[!] Accessing Database!')

    conn = sqlite3.connect('./Database/test_DB.db')

    cursor = conn.execute("SELECT UID,EMAIL from USERS WHERE EMAIL='"+user_email+"'")
    users_email_check = cursor.fetchall()

    if not users_email_check:
        conn.execute("INSERT INTO USERS (UID,FIRST_NAME,LAST_NAME,EMAIL,PHONE_NUM,PASSWORD) \
              VALUES ('"+UID+"','"+first_name+"','"+last_name+"','"+user_email+"','"+phone_number+"','"+password+"')")

        conn.commit()
        conn.close()
        print('[+] User Created')
        return "0"
    else:
        conn.close()
        print('[+] User Email Already In Use')
        return "1"
