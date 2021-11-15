import json
import sqlite3
import datetime
import re




def get_staff():
    print('[!] Accessing Database!')

    conn = sqlite3.connect('/usr/src/app/Backend/Database/test_DB.db')
    cursor = conn.execute("SELECT UID,FIRST_NAME,LAST_NAME,EMAIL,PHONE_NUM,SALARY,PASSWORD from ADMIN")

    staff = {}
    count = 0
    for row in cursor:


        staff[count] = {"UID": row[0],"FIRST_NAME":row[1],"LAST_NAME":row[2],"EMAIL":row[3],"PHONE_NUM":row[4],"SALARY":row[5],"PASSWORD":row[6]}
        count += 1


    conn.commit()
    conn.close()

    staff_json = json.dumps(staff)
    print("[+] Packaged All Staff into JSON Format")
    return staff_json
