import json
import sqlite3
import datetime
import re


def login(user_email, user_password):
    try:
        print('[!] Accessing Database!')

        conn = sqlite3.connect('/usr/src/app/Backend/Database/test_DB.db')


        cursor = conn.execute("SELECT UID from USERS WHERE EMAIL='"+user_email+"' AND PASSWORD='"+user_password+"'")
        row = cursor.fetchall()


        try:
            UID = str(row[0][0])
            code = "0"
            print("[+] FOUND USER!")
        except:
            UID = "NONE"
            code = "1"

        conn.commit()
        conn.close()

        return code,UID
    except:
        conn.close()
