#!/usr/bin/python

import logging

from vmarket import market

logging_cfg			= {
    "level":	logging.DEBUG,
    "datefmt":	'%m-%d %H:%M:%S',
    "format":	'%(asctime)s.%(msecs).03d %(threadName)10.10s %(name)-15.15s %(funcName)-15.15s %(levelname)-8.8s %(message)s',
}
logging.basicConfig( **logging_cfg )

seller_id	= 1
buyer_id	= 2

west		= market("West Market")
item_id		= west.post( seller_id,
                             description	= """I have a long hair that I want to sell for 100 pennies per ounce.""",
                             quantity		= 20 )
print west[item_id]