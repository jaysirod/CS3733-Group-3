import json
import sqlite3
import datetime
import re




def update_staff(UID,first_name,last_name,email,phone_number,salary):
    try:
        print('[!] Accessing Database!')

        conn = sqlite3.connect('/usr/src/app/Backend/Database/test_DB.db')

        cursor = conn.execute("SELECT UID , EMAIL from ADMIN WHERE EMAIL='"+email+"'")
        admin_email = cursor.fetchall()
        if len(admin_email) != 0:
            if admin_email[0][0] != UID:
                conn.close()
                return "1"




        cursor = conn.execute("UPDATE ADMIN SET FIRST_NAME = '"+first_name+"', LAST_NAME = '"+last_name+"',EMAIL='"+email+"' ,PHONE_NUM='"+phone_number+"',SALARY ='"+salary+"' WHERE UID="+str(UID))
        conn.commit()
        conn.close()

        print('[!] Successfully Finished Staff Member Update')
        return "0"
    except:
        conn.close()
