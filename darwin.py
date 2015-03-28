#!/usr/bin/env python

import time
import sys
import logging
import stomp
import zlib

logging.basicConfig()

if len(sys.argv) < 4:
	print 'Usage: python darwin.py stomp_username stomp_password queue_name'
	quit()

user = sys.argv[1]
pwd = sys.argv[2]
queue_name = sys.argv[3]
class MyListener(object):
    def on_error(self, headers, message):
        print('received an error %s' % message)
    def on_message(self, headers, message):
    	data=zlib.decompress(message, 16+zlib.MAX_WBITS)
        print('received a message %s' % data)

conn=stomp.Connection([('datafeeds.nationalrail.co.uk',61613)])
conn.set_listener('', MyListener())
conn.start()
conn.connect(user,pwd)

conn.subscribe(destination='/queue/' + queue_name, id=1, ack='auto')

time.sleep(1)
conn.disconnect()