import json
import sqlite3
import datetime
import re




def create_user(UID,first_name,last_name,user_email,phone_number,password):

    print('[!] Accessing Database!')

    conn = sqlite3.connect('./Database/test_DB.db')


    conn.execute("INSERT INTO USERS (UID,FIRST_NAME,LAST_NAME,EMAIL,PHONE_NUM,PASSWORD) \
          VALUES ('"+UID+"','"+first_name+"','"+last_name+"','"+user_email+"','"+phone_number+"','"+password+"')")

    conn.commit()
    conn.close()
    print('[+] User Created')
    return "0"
