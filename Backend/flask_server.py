from flask import Flask
import requests
import os
from flask import request
import json
from flask_cors import CORS
from flask import flash, redirect, url_for
from werkzeug.utils import secure_filename
from flask import render_template

import get_hotels
import get_hotel_info
import admin_get_hotels
import admin_get_hotel_info
import update_hotel
import get_staff
import delete_hotel
import add_hotel
import id_generator
import get_staff_info
import update_staff
import delete_staff
import add_staff
import admin_analytics

app = Flask(__name__)
CORS(app)

'''
FUNCTIONS

*NOTE* Each function should tell if the user is a 'Guest'(Not logged in), 'User', or 'Admin'

Each function will get a request from the website and the function will return with the
proper data

- Add User (User creates an account)
- Add Admin (Admin adds admin)
- Add Hotel (Admin adds hotel)

- Modify User information (change name, change password, etc)
- Modify Admin information (Change role, change name, etc)
- Modify Hotel Information (Change prices, change rooms, etc)
- Modify Hotel price for weekends

- Delete User (User deletes account)
- Delete Admin (Admin removes another admin (Fired or quit))
- Delete Reservation (User Deletes reservation)

- Get Reservations (User Views all reservations, function returns past or future)
- Get Hotel's Reservation total (Admin views individual hotel analytics) (Admin analytics view)

- Make reservation (User or admin can make a reservation)
- Make purchase (Simulate online transaction)



'''

@app.route('/')
def main_page():
    return 'V Hotels Web Application V1'


'''
------------- get_hotels_user -------------
Get Hotels (User's search, adjusts to filters) (Hotel Search Page)


Description:
    This function is responsible for receiving the information
    given by the user. This function will mainly be used when the
    user is searching for a hotel to reserve. This function will make
    sure the user will receive hotels that meet the requirements

Rules:
    The user can only make a reservation with a proper date range and
    with the rooms being available for the hotel. When making the
    reservation we want to display the hotels that meet the wants of
    the user, such as anemities.

'''
@app.route('/hotels')
def get_hotels_user():
    print('[+] User Requested Hotels')
    start_date = request.args.get('start_date',type=str)
    end_date = request.args.get('end_date',type=str)
    user_amenities = request.args.get('user_amenities',type=str).split(',')
    lowest_price = request.args.get('lowest_price',type=str)
    highest_price = request.args.get('highest_price',type=str)

    hotels_json = get_hotels.user_get_hotels(start_date,end_date,user_amenities,lowest_price,highest_price)
    print('[+] Finised User Hotel Request... Sending Data Now!')
    return hotels_json

'''
------------- get_hotel_information -------------

Get Hotel information (Rooms, prices, images, etc) (Hotel Page, when viewing individual hotel)

Description:
    This function will retrive all information for a given hotel. This function
    will mainly be used in the hotel_page, where the user can view the Information
    of a hotel.

'''
@app.route('/hotel_info')
def get_hotel_information():
    HID = request.args.get('HID',type=str) #Range of reservation
    print('[+] Get Hotel Information For : '+str(HID))

    start_date = request.args.get('start_date',type=str)
    end_date = request.args.get('end_date',type=str)

    hotels_json = get_hotel_info.get_hotel_info(HID,start_date,end_date)


    print('[+] Finised User Hotel Request... Sending Data Now!')
    return hotels_json

@app.route('/admin_hotels')
def admin_get_hotels_req():

    print('[+] Admin Requested Hotels')

    hotels_json = admin_get_hotels.get_hotels_admin()

    print('[+] Finised Admin Hotel Request... Sending Data Now!')
    return hotels_json



@app.route('/admin_hotel_info')
def admin_get_hotel_info_req():

    HID = request.args.get('HID',type=str) #Range of reservation
    print('[+] Admin Get Hotel Information For : '+str(HID))

    hotels_json = admin_get_hotel_info.get_hotel_info(HID)
    print('[+] Finised Admin Hotel Request... Sending Data Now!')
    return hotels_json



@app.route('/update_hotel')
def admin_update_hotel():

    print('[+] Admin Updating Hotel Info')

    HID = request.args.get('HID',type=str)
    hotel_name = request.args.get('hotel_name',type=str)
    num_of_rooms = request.args.get('num_of_rooms',type=str)
    hotel_img = request.args.get('hotel_img',type=str)
    weekend_percent = request.args.get('weekend_percent',type=str)
    phone_number = request.args.get('phone_number',type=str)
    standard_image = request.args.get('standard_image',type=str)
    standard_price = request.args.get('standard_price',type=str)
    queen_image = request.args.get('queen_image',type=str)
    queen_price = request.args.get('queen_price',type=str)
    king_image = request.args.get('king_image',type=str)
    king_price = request.args.get('king_price',type=str)
    amenities = request.args.get('amenities',type=str).split(',')
    amenities_availability = request.args.get('amenities_availability',type=str).split(',')

    update_code = update_hotel.update_hotel(HID,hotel_name,num_of_rooms,hotel_img,weekend_percent,phone_number,standard_image,standard_price,queen_image,queen_price,king_image,king_price,amenities,amenities_availability)

    return update_code

@app.route('/uploader', methods = ['POST'])
def success():
    if request.method == 'POST':
        hotel_img = request.files['hotel_img']
        standard_img = request.files['standard_img']
        queen_img = request.files['queen_img']
        king_img = request.files['king_img']

        try:
            hotel_img.save('../hotel_images/'+hotel_img.filename)
        except:
            pass

        try:
            standard_img.save('../hotel_room_images/'+standard_img.filename)
        except:
            pass

        try:
            queen_img.save('../hotel_room_images/'+queen_img.filename)
        except:
            pass

        try:
            king_img.save('../hotel_room_images/'+king_img.filename)
        except:
            pass

        return render_template("index.html")


@app.route('/delete_hotel')
def admin_delete_hotel():

    print('[!] WARNING : Admin Deleting Hotel')
    HID = request.args.get('HID',type=str)
    code = delete_hotel.delete_hotel(HID)
    print('[!] Deleted Hotel')
    return code


@app.route('/add_hotel')
def admin_add_hotel():

    print('[!] Admin Adding Hotel')

    HID = str(id_generator.hotel_id_generate())
    hotel_name = request.args.get('hotel_name',type=str)
    num_of_rooms = request.args.get('num_of_rooms',type=str)
    hotel_img = request.args.get('hotel_img',type=str)
    weekend_percent = request.args.get('weekend_percent',type=str)
    phone_number = request.args.get('phone_number',type=str)
    standard_image = request.args.get('standard_image',type=str)
    standard_price = request.args.get('standard_price',type=str)
    queen_image = request.args.get('queen_image',type=str)
    queen_price = request.args.get('queen_price',type=str)
    king_image = request.args.get('king_image',type=str)
    king_price = request.args.get('king_price',type=str)
    amenities = request.args.get('amenities',type=str).split(',')
    amenities_availability = request.args.get('amenities_availability',type=str).split(',')

    code = add_hotel.add_hotel(HID,hotel_name,num_of_rooms,hotel_img,weekend_percent,phone_number,standard_image,standard_price,queen_image,queen_price,king_image,king_price,amenities,amenities_availability)
    print('[!] Added Hotel')
    return code



@app.route('/admin_staff')
def admin_get_staff():

    print('[+] Admin Get Staff')

    staff_json = get_staff.get_staff()
    print('[+] Finised Admin Staff Request... Sending Data Now!')
    return staff_json


@app.route('/admin_staff_info')
def admin_get_staff_info():

    print('[+] Admin Get Staff Info')
    UID = request.args.get('UID',type=str)

    staff_json = get_staff_info.get_staff_info(UID)
    print('[+] Finised Admin Staff Request... Sending Data Now!')
    return staff_json


@app.route('/update_staff_info')
def admin_update_staff_info():

    print('[+] Admin Get Staff Info')
    UID = request.args.get('UID',type=str)
    first_name = request.args.get('first_name',type=str)
    last_name = request.args.get('last_name',type=str)
    email = request.args.get('member_email',type=str)
    phone_number = request.args.get('phone_number',type=str)
    salary = request.args.get('salary',type=str)

    staff_json = update_staff.update_staff(UID,first_name,last_name,email,phone_number,salary)
    print('[+] Finised Admin Staff Request... Sending Data Now!')
    return staff_json

@app.route('/delete_staff_member')
def admin_delete_staff_member():

    print('[+] WARNING : Admin Staff Deletion')
    UID = request.args.get('UID',type=str)

    code = delete_staff.delete_staff(UID)
    print('[+] Finised Admin Staff Deletion')
    return code



@app.route('/add_staff_member')
def admin_add_staff_member():

    print('[+] Admin Adding Staff Member')
    UID = str(id_generator.admin_id_generate())
    first_name = request.args.get('first_name',type=str)
    last_name = request.args.get('last_name',type=str)
    email = request.args.get('member_email',type=str)
    phone_number = request.args.get('phone_number',type=str)
    salary = request.args.get('salary',type=str)
    password = request.args.get('password',type=str)

    code = add_staff.add_staff(UID,first_name,last_name,email,phone_number,salary,password)
    print('[+] Finised Adding Staff Member')
    return code


@app.route('/get_reservations_analytics')
def admin_get_reservation_analytics():
    print('[+] Admin Retriving Reservations')

    time_period = request.args.get('time_period',type=str)
    hotel_id = request.args.get('hotel_id',type=str)

    reservations_json = admin_analytics.get_reservations(time_period,hotel_id)
    print('[+] Admin Sending Reservations')

    return reservations_json


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)
