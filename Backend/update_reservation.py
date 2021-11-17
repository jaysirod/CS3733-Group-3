import json
import sqlite3
import datetime
import re


import smtplib
import imghdr
from email.message import EmailMessage
from email.mime.multipart import MIMEMultipart #pip install email-to
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def send_email(user_name,user_email,hotel_image,hotel_name,checkin,checkout,adults,children,price,reservation_id):

    EMAIL_ADDRESS = "vhotels.project@gmail.com"
    EMAIL_PASSWORD = "@Test12345"

    with open("/usr/src/app/"+hotel_image, 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = 'hotel_image.jpg'


    msg = EmailMessage()
    msg['Subject'] = 'Your Reservation Details!'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = user_email
    #msg['To'] = (", ").join(contacts) #use this if you want to have multiple recipients in the same email
    msg.set_content('Your Reservation Details')
    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename = file_name)

    text_part,attachment_part = msg.iter_parts()
    text_part.add_alternative("""\
    <!DOCTYPE html>
    <html>
        <body>
            <center><h1>"""+user_name+""", Your reservation is confirmed!</h1></center>
            <center><h3>You are going to Texas!</h3></center>
            <center><h2>"""+hotel_name+"""</h2></center>
            <br>
            <center><img src="cid:image1" style="width:300px;height:300px;"></img></center>
            <hr>
            <br>
            <center><h2>Your Reservation Details:</h2></center>
            <center><p style="font-size:15px;">Check-In : """+checkin+"""</p></center>
            <center><p style="font-size:15px;">Check-Out : """+checkout+"""</p></center>
            <center><p style="font-size:15px;">Adults : """+adults+""" , Children : """+children+"""</p></center>
            <center><p style="font-size:15px;">Price : $"""+price+"""</p></center>
            <center><p style="font-size:15px;">Reservation ID : """+reservation_id+"""</p></center>

            <br>
            <center><p>When you arrive please make sure to check-in at the front desk. You will provide your Reservation ID at the front desk</p></center>
        </body>
    </html>



    """, subtype='html')

    fp = open("/usr/src/app/"+hotel_image, 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()

    # Define the image's ID as referenced above
    msgImage.add_header('Content-ID', '<image1>')
    msg.attach(msgImage)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)


    print('[+] Email Sent')




def create_date(date_string):
    #CONSISTANT FORMAT yyyy-mm-dd : EXAMPLE: 2/4/2021 or 12/12/2021

    processed_date = re.search(r'([0-9]*)-([0-9]*)-([0-9]*)', date_string)


    month = int(processed_date.group(2))
    day = int(processed_date.group(3))
    year = int(processed_date.group(1))

    date = datetime.datetime(year,month,day)

    return date


def is_room_available(conn,HID,start_date,end_date,num_of_rooms,room_type,distribution):
    cursor = conn.execute("SELECT HID,UID,RID,ROOM_TYPE,START_DATE,END_DATE from RESERVATIONS")

    if distribution == 3:
        # out of total num rooms = 50% will be standard , 30% will be Queen, and 20% will be King = 100% total
        if str(room_type) == "Standard":
            num_of_rooms = int(int(num_of_rooms) * 0.50)
        elif str(room_type) == "Queen":
            num_of_rooms = int(int(num_of_rooms) * 0.30)
        elif str(room_type) == "King":
            num_of_rooms = int(int(num_of_rooms) * 0.20)
    elif distribution == 2:
        # 50% split between two rooms
        num_of_rooms = int(int(num_of_rooms) * 0.50)
    elif distribution == 1:
        # one room will contain all of the available rooms 100%
        num_of_rooms = int(int(num_of_rooms) * 1)


    #traverse through all of reservations.
    conn.commit()
    for row in cursor:
        if str(HID) == str(row[0]) and str(room_type) == str(row[3]):
            user_start_date = create_date(start_date)
            user_end_date = create_date(end_date)
            reservation_start_date = create_date(row[4])
            reservation_end_date = create_date(row[5])

            #if there is a reservation already conflicting with the time period then decrese the number of rooms
            if not ((user_start_date.date() > reservation_start_date.date() and user_start_date.date() > reservation_end_date.date()) or (user_end_date.date() < reservation_start_date.date() and user_end_date.date() < reservation_end_date.date())):
                num_of_rooms -= 1
                if num_of_rooms == 0:
                    return False
    return True


def update_user_reservation(RID,user_email,first_name,last_name,room_type,start_date,end_date,adult_num,children_num):
    try:
        conn = sqlite3.connect('/usr/src/app/Backend/Database/test_DB.db')

        cursor = conn.execute("SELECT HID,UID,RID,ROOM_TYPE,START_DATE,PRICE,EMAIL,FIRST_NAME,LAST_NAME,NUM_ADULTS,NUM_CHILDREN,END_DATE from RESERVATIONS WHERE RID ='"+str(RID)+"'")
        row_reservation = cursor.fetchall()

        HID = row_reservation[0][0]
        cursor_hotel = conn.execute("SELECT HID,NAME,NUM_OF_ROOMS,IMG_URL,PHONE_NUMBER from HOTEL WHERE HID ='"+str(HID)+"'")
        row_hotel = cursor_hotel.fetchall()

        cursor_hotel_rooms = conn.execute("SELECT HID,NUM,TYPE,IMG_URL,PRICE from HOTEL_ROOM WHERE HID ='"+str(HID)+"' AND TYPE = '"+str(room_type)+"'")
        row_hotel_rooms = cursor_hotel_rooms.fetchall()

        end_date_datetime = create_date(end_date)
        start_date_datetime = create_date(start_date)

        num_nights = int((end_date_datetime.date() - start_date_datetime.date()).days)
        price = str(round(float(((int(row_hotel_rooms[0][4]) * 0.0825) + int(row_hotel_rooms[0][4])) * num_nights), 2))

        cursor_hotel_rooms_dist = conn.execute("SELECT HID,NUM,TYPE,IMG_URL,PRICE from HOTEL_ROOM WHERE HID ='"+str(HID)+"'")

        rooms_available = 0
        for row in cursor_hotel_rooms_dist:
            if str(row[4]) != "999999":
                rooms_available += 1


        if is_room_available(conn,HID,start_date,end_date,int(row_hotel[0][2]),room_type,rooms_available):
            conn.execute("UPDATE RESERVATIONS SET ROOM_TYPE = '"+room_type+"',START_DATE = '"+start_date+"',PRICE = '"+str(price)+"',EMAIL = '"+user_email+"',FIRST_NAME = '"+first_name+"',LAST_NAME = '"+last_name+"',NUM_ADULTS = '"+adult_num+"',NUM_CHILDREN = '"+children_num+"',END_DATE = '"+end_date+"' WHERE RID='"+str(RID)+"'")
            conn.commit()
            conn.close()

            send_email(first_name,user_email,row_hotel[0][3],row_hotel[0][1],start_date,end_date,adult_num,children_num,price,RID)

            print("[+] Successfully Updated Reservation")

            return "0"
        else:
            conn.close()
            print("[+] Failed to Update Reservation")

            return "1"
    except:
        conn.close()
