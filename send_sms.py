#!/usr/bin/python
#coding: utf-8

# OpenSMS - Send de SMS

from time import sleep
from threading import Thread
from smsKhomp import sendSMS
from dbconnect import select

charge = select("select id, telefone, msg from torpedos_khomp where status <> '<K> Message sent successfully!' limit 5")

ebs = 0
channel = 0
lote = 0

for sms in charge:

    task = Thread(target=sendSMS, args=(sms, ebs, channel,))
    task.start()

    #rule for sending SMS to channels of EBS khomp
    if ebs == 3 and channel == 15:
        lote += 1
        print("%s lote enviado para khomp" % lote)
        ebs = 0
        channel = 0
        sleep(30)

    if channel == 15:
        ebs += 1
        channel = 0
    
    channel += 1