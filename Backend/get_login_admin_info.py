import json
import sqlite3
import datetime
import re



def verify(UID):

    print('[!] Accessing Database!')

    conn = sqlite3.connect('/usr/src/app/Backend/Database/test_DB.db')


    cursor = conn.execute("SELECT FIRST_NAME from ADMIN WHERE UID='"+UID+"'")
    row = cursor.fetchall()


    try:
        name = str(row[0][0])
        code = "0"
        print("[+] FOUND USER!")
    except:
        name = "NONE"
        code = "1"

    conn.commit()
    conn.close()

    return code,name
