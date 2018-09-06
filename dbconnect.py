#!/usr/bin/python
#coding: utf-8

#OpenSMS - Send de SMS

import pymysql.cursors

def connect():
    connection = pymysql.connect(host='192.168.25.24',
                                 user='robo',
                                 password='@#3rL9.!',
                                 db='crm_vicoa',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection


def select(query):

    cur = connect()
    curs = cur.cursor()
    curs.execute(query)
    return curs.fetchall()
