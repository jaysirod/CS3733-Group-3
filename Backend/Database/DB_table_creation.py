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
         WEEKEND_PERCENT  TEXT    NOT NULL,
         PHONE_NUMBER     INT     NOT NULL);''')


conn.execute('''CREATE TABLE AMENITIES
         (HID             TEXT     NOT NULL,
         TYPE             TEXT    NOT NULL,
         AVAILABILITY     TEXT     NOT NULL);''')

conn.execute('''CREATE TABLE HOTEL_ROOM
         (HID             TEXT     NOT NULL,
         NUM              TEXT    NOT NULL,
         TYPE             TEXT     NOT NULL,
         IMG_URL          TEXT    NOT NULL,
         PRICE            INT     NOT NULL);''')

conn.execute('''CREATE TABLE RESERVATIONS
         (HID             TEXT     NOT NULL,
         UID              TEXT    NOT NULL,
         RID              TEXT     NOT NULL,
         ROOM_TYPE        TEXT   NOT NULL,
         START_DATE       TEXT     NOT NULL,
         PRICE            TEXT    NOT NULL,
         EMAIL            TEXT    NOT NULL,
         FIRST_NAME            TEXT    NOT NULL,
         LAST_NAME            TEXT    NOT NULL,
         NUM_ADULTS            TEXT    NOT NULL,
         NUM_CHILDREN            TEXT    NOT NULL,
         END_DATE         TEXT     NOT NULL);''')



conn.close()
