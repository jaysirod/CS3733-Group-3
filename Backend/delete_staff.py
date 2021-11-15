import json
import sqlite3
import datetime
import re




def delete_staff(UID):
    print('[!] Accessing Database!')

    conn = sqlite3.connect('/usr/src/app/Backend/Database/test_DB.db')
    conn.execute("DELETE FROM ADMIN WHERE UID='"+str(UID)+"'")
    conn.commit()
    conn.close()

    print('[!] Successfully Deleted Staff Member')
    return "0"
