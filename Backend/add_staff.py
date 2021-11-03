import json
import sqlite3
import datetime
import re






def add_staff(UID,first_name,last_name,email,phone_number,salary,password):
    conn = sqlite3.connect('./Database/test_DB.db')
    print("Opened database successfully")


    cursor = conn.execute("SELECT UID,EMAIL from ADMIN WHERE EMAIL='"+email+"'")
    admin_email_check = cursor.fetchall()

    if not admin_email_check:
        conn.execute("INSERT INTO ADMIN (UID,FIRST_NAME,LAST_NAME,EMAIL,PHONE_NUM,SALARY,PASSWORD) \
              VALUES ('"+UID+"', '"+first_name+"', '"+last_name+"', '"+email+"', '"+phone_number+"','"+salary+"','"+password+"')")

        conn.commit()
        conn.close()

        print('[!] Successfully Added Staff')
        return "0"
    else:
        conn.close()
        print('[+] User Email Already In Use')
        return "1"
