#!/usr/bin/python

import os, sys

scriptdir	= os.path.dirname(os.path.abspath(__file__)) # clip file name from path
basedir		= os.path.dirname(scriptdir) # tests/..

sys.path.insert(0, basedir)

import logging

from vmarket	import market
from utils	import setup

log		= setup.logging( name=__file__, level=logging.DEBUG )

seller_id	= 1
buyer_id	= 2

def test_basic():
    
    west		= market("West Market")
    item_id		= west.post( seller_id,
                                     description	= """I have a long hair that I want to sell for 100 pennies per ounce.""",
                                     quantity		= 20 )
    assert west[item_id]

    log.info("Created item_id: %s with values %r", item_id, west[item_id])
