import json
import sqlite3
import datetime
import re



def update(UID,user_email,first_name,last_name,phone_number):
    try:
        print('[!] Accessing Database!')

        conn = sqlite3.connect('/usr/src/app/Backend/Database/test_DB.db')

        cursor = conn.execute("SELECT UID , EMAIL from USERS WHERE EMAIL='"+user_email+"'")
        email_user = cursor.fetchall()
        if len(email_user) != 0:
            if email_user[0][0] != UID:
                conn.close()
                return "1"


        cursor = conn.execute("UPDATE USERS SET FIRST_NAME = '"+first_name+"', LAST_NAME = '"+last_name+"',EMAIL='"+user_email+"' ,PHONE_NUM='"+phone_number+"' WHERE UID="+str(UID))
        conn.commit()
        conn.close()

        print('[!] Successfully Finished User Update')
        return "0"
    except:
        conn.close()
