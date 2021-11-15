import json
import sqlite3
import datetime
import re




def get_user(UID):
    try:
        print('[!] Accessing Database!')

        conn = sqlite3.connect('/usr/src/app/Backend/Database/test_DB.db')
        cursor = conn.execute("SELECT UID,FIRST_NAME,LAST_NAME,EMAIL,PHONE_NUM from USERS WHERE UID='"+str(UID)+"'")
        row_user = cursor.fetchall()

        user_info = {}
        user_info[0] = {"UID": row_user[0][0],"FIRST_NAME":row_user[0][1],"LAST_NAME":row_user[0][2],"EMAIL":row_user[0][3],"PHONE_NUM":row_user[0][4]}


        conn.commit()
        conn.close()

        user_info_json = json.dumps(user_info)
        print("[+] Packaged User Info to JSON Format")
        return user_info_json
    except:
        conn.close()
