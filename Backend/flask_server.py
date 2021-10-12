from flask import Flask
import requests
import os
from flask import request
import json
from flask_cors import CORS


import get_hotels



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


- Delete User (User deletes account)
- Delete Admin (Admin removes another admin (Fired or quit))
- Delete Reservation (User Deletes reservation)

- Get Reservations (User Views all reservations, function returns past or future)
- Get Hotel information (Rooms, prices, images, etc) (Hotel Page, when viewing individual hotel)
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
    date_range = request.args.get('date_range',type=str) #Range of reservation
    anemities = request.args.get('anemities',type=str) #pool,gym,etc
    price = request.args.get('price',type=str) #range or max price

    hotels_json = get_hotels.user_get_hotels(date_range,anemities,price)
    print('[+] Finised User Hotel Request... Sending Data Now!')
    return hotels_json



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)
