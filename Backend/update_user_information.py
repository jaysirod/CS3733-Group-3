import json
import sqlite3
import datetime
import re



def update(UID,user_email,first_name,last_name,phone_number):
    print('[!] Accessing Database!')

    conn = sqlite3.connect('./Database/test_DB.db')
    cursor = conn.execute("UPDATE USERS SET FIRST_NAME = '"+first_name+"', LAST_NAME = '"+last_name+"',EMAIL='"+user_email+"' ,PHONE_NUM='"+phone_number+"' WHERE UID="+str(UID))
    conn.commit()
    conn.close()

    print('[!] Successfully Finished User Update')
    return "0"
