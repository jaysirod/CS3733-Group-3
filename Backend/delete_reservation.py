import json
import sqlite3
import datetime
import re

#Deletes reservations from database
def delete_reservation(RID):
    try:
        conn = sqlite3.connect('/usr/src/app/Backend/Database/test_DB.db')
        conn.execute("DELETE FROM RESERVATIONS WHERE RID='"+str(RID)+"'")
        conn.commit()
        conn.close()


        return "0"
    except:
        conn.close()
