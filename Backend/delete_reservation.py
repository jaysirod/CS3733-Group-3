import json
import sqlite3
import datetime
import re





def delete_reservation(RID):

    conn = sqlite3.connect('/usr/src/app/Backend/Database/test_DB.db')
    conn.execute("DELETE FROM RESERVATIONS WHERE RID='"+str(RID)+"'")
    conn.commit()
    conn.close()


    return "0"
