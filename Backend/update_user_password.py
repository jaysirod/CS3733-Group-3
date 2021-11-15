import json
import sqlite3
import datetime
import re




def update(UID,new_password,old_password):
    print('[!] Accessing Database!')

    conn = sqlite3.connect('/usr/src/app/Backend/Database/test_DB.db')

    cursor_user = conn.execute("SELECT PASSWORD from USERS WHERE UID='"+UID+"'")
    row_user = cursor_user.fetchall()

    try:
        if str(row_user[0][0]) == str(old_password):
            cursor = conn.execute("UPDATE USERS SET PASSWORD = '"+new_password+"' WHERE UID='"+str(UID)+"'")
            conn.commit()
            conn.close()

            print('[!] Successfully Finished User Update')
            return "0"
        else:
            conn.commit()
            conn.close()
            return "1"
    except:
        conn.commit()
        conn.close()
        print('[!] Failed To Update User Password')
        return "1"
