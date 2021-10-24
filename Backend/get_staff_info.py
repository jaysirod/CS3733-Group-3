import json
import sqlite3
import datetime
import re




def get_staff_info(UID):
    print('[!] Accessing Database!')

    conn = sqlite3.connect('./Database/test_DB.db')
    cursor = conn.execute("SELECT FIRST_NAME,LAST_NAME,EMAIL,PHONE_NUM,SALARY from ADMIN WHERE UID = "+str(UID))

    staff = {}
    row = cursor.fetchall()

    staff[0] = {"FIRST_NAME":row[0][0],"LAST_NAME":row[0][1],"EMAIL":row[0][2],"PHONE_NUM":row[0][3],"SALARY":row[0][4]}


    conn.commit()
    conn.close()

    staff_json = json.dumps(staff)
    print("[+] Packaged All Staff into JSON Format")
    return staff_json
