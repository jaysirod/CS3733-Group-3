from flask import Flask
import requests
import os
from flask import request


app = Flask(__name__)

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
- Get Hotels (User's search, adjusts to filters) (Hotel Search Page)
- Get Hotel information (Rooms, prices, images, etc) (Hotel Page, when viewing individual hotel)
- Get Hotel's Reservation total (Admin views individual hotel analytics) (Admin analytics view)

- Make reservation (User or admin can make a reservation)
- Make purchase (Simulate online transaction)

'''

@app.route('/')
def main_page():
    return 'V Hotels Web Application V1'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)
