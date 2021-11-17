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

#Sends email when account is created
def send_email(user_email,user_name):
    EMAIL_ADDRESS = "vhotels.project@gmail.com"
    EMAIL_PASSWORD = "@Test12345"

    with open('/usr/src/app/email_images/VHotels-Logo-Black.png', 'rb') as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)
        file_name = 'VHotels-Logo-Black.png'


    msg = EmailMessage()
    msg['Subject'] = 'VHotels Account Creation'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = user_email
    #msg['To'] = (", ").join(contacts) #use this if you want to have multiple recipients in the same email
    msg.set_content('Account Successfully Registered')
    msg.add_attachment(file_data, maintype='image', subtype=file_type, filename = file_name)

    text_part,attachment_part = msg.iter_parts()
    text_part.add_alternative("""\
    <!DOCTYPE html>
    <html>
        <body>

            <center><img src="cid:image1" style="width:150px;height:300px;"></img></center>
            <hr>
            <br>
            <center><h2>Welcome """+user_name+"""!</h2></center>
            <center><p style="font-size:15px;">Congratulations """+user_name+""", you have been added to the admin team!</p></center>

            <br>
        </body>
    </html>




    """, subtype='html')

    fp = open('/usr/src/app/email_images/VHotels-Logo-Black.png', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()

    # Define the image's ID as referenced above
    msgImage.add_header('Content-ID', '<image1>')
    msg.attach(msgImage)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

#Admistration: Add Staffs to database
def add_staff(UID,first_name,last_name,email,phone_number,salary,password):
    try:
        conn = sqlite3.connect('/usr/src/app/Backend/Database/test_DB.db')
        print("Opened database successfully")


        cursor = conn.execute("SELECT UID,EMAIL from ADMIN WHERE EMAIL='"+email+"'")
        admin_email_check = cursor.fetchall()

        if not admin_email_check:
            conn.execute("INSERT INTO ADMIN (UID,FIRST_NAME,LAST_NAME,EMAIL,PHONE_NUM,SALARY,PASSWORD) \
                  VALUES ('"+UID+"', '"+first_name+"', '"+last_name+"', '"+email+"', '"+phone_number+"','"+salary+"','"+password+"')")

            conn.commit()
            conn.close()
            send_email(email,first_name)
            print('[!] Successfully Added Staff')
            return "0"
        else:
            conn.close()
            print('[+] User Email Already In Use')
            return "1"
    except:
        conn.close()
