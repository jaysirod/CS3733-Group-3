#!/usr/bin/python

import sqlite3

conn = sqlite3.connect('test_DB.db')

conn.execute('''CREATE TABLE USERS
         (UID INT PRIMARY KEY     NOT NULL,
         FIRST_NAME       TEXT    NOT NULL,
         LAST_NAME        TEXT    NOT NULL,
         EMAIL                    CHAR(50),
         PHONE_NUM        INT     NOT NULL,
         PASSWORD       CHAR(30));''')

conn.execute('''CREATE TABLE ADMIN
         (UID INT PRIMARY KEY     NOT NULL,
         FIRST_NAME       TEXT    NOT NULL,
         LAST_NAME        TEXT    NOT NULL,
         EMAIL                    CHAR(50),
         PHONE_NUM        INT     NOT NULL,
         SALARY           INT     NOT NULL,
         PASSWORD       CHAR(30));''')

conn.execute('''CREATE TABLE HOTEL
         (HID INT PRIMARY KEY     NOT NULL,
         NAME             TEXT    NOT NULL,
         NUM_OF_ROOMS     INT     NOT NULL,
         IMG_URL          TEXT    NOT NULL,
         PHONE_NUMBER     INT     NOT NULL);''')


conn.execute('''CREATE TABLE AMENITIES
         (HID             INT     NOT NULL,
         TYPE             TEXT    NOT NULL,
         AVAILABILITY     INT     NOT NULL);''')

conn.execute('''CREATE TABLE HOTEL_ROOM
         (HID             INT     NOT NULL,
         NUM              TEXT    NOT NULL,
         TYPE             INT     NOT NULL,
         IMG_URL          TEXT    NOT NULL,
         PRICE            INT     NOT NULL);''')

conn.execute('''CREATE TABLE RESERVATIONS
         (HID             INT     NOT NULL,
         UID              TEXT    NOT NULL,
         RID              INT     NOT NULL,
         START_DATE       INT     NOT NULL,
         END_DATE         INT     NOT NULL);''')



conn.close()
