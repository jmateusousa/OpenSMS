#!/usr/bin/python
#coding: utf-8

#OpenSMS - Send de SMS

import os
from subprocess import call, getstatusoutput
from time import sleep, strftime
from dbconnect import connect
from threading import Thread


def sendSMS(sms, ebs=0, channel=0):

    db = connect()
    cur = db.cursor()

    ebschannel = "B" + str(ebs) + "C" + str(channel)

    if len(sms) >= 1:
        
        ksend = call('asterisk -rx "khomp sms %s %s %s"' % (ebschannel, sms['telefone'], sms['msg']), shell=True)
        outprocess = getstatusoutput('asterisk -rx "khomp sms %s %s %s"' % (ebschannel, sms['telefone'], sms['msg']))

        data = "%s" % (strftime("%Y_%m_%d"))

        if 'ERROR' in outprocess[1] :
            status = '{}'.format(outprocess[1][0:63])
            print(status, sms['id'])
            update_torperdo = "UPDATE torpedos_khomp set data_envio = '%s', status = '%s' where id = '%s'" % (data, status, sms['id'])
            cur.execute(update_torperdo)
            db.commit()
        
        else:
            status = '{}'.format(outprocess[1])
            update_torperdo = "UPDATE torpedos_khomp set data_envio = '%s', status = '%s' where id = '%s'" % (data, status, sms['id'])
            cur.execute(update_torperdo)
            db.commit()
        
    else:
        print("Erro!")
