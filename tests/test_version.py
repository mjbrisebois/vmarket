#!/usr/bin/python

import os, sys, json

scriptdir	= os.path.dirname(os.path.abspath(__file__)) # clip file name from path
basedir		= os.path.dirname(scriptdir) # tests/..

sys.path.insert(0, basedir)

import logging

from vmarket		import market
from utils		import setup
from utils.version	import Version
from collections	import OrderedDict

import json

log		= setup.logging( name=__file__, level=logging.DEBUG )

def test_version_sort():
    versions		= Version()
    print versions
    versions['1.11.a']	= []
    versions['1.2-r']	= []
    versions['2.1']	= []
    versions['9.a-20']	= []
    versions['9.a-10']	= []
    versions['1.11.2']	= []
    versions['1.11.1']	= []
    versions['1.2-b2']	= []
    versions['2.b']	= []
    versions['2.100']	= []
    versions['1']	= []
    versions['1.2-rc3']	= []
    versions['9.a-2']	= []
    versions['1.10-rc3']= []
    versions['1.10']	= []
    versions['2.a']	= []
    versions['1.11.b']	= []
    versions['1.2-r5']	= []
    versions['1.11']	= []
    versions['9.a-1']	= []
    versions['9.1-1']	= []
    versions['9.1-2']	= []
    versions['9.1-10']	= []
    versions['9.2-a']	= []
    versions['9.2-1']	= []
    versions['9.2-b']	= []
    versions['9.10-44']	= []
    versions['9.10-45']	= []
    versions['10.2']	= []
    versions['1.2-a1']	= []
    versions['10.10']	= []

    # 1.2.0.1 instead of 1.2-a1
    # 1.2.1.2 instead of 1.2-b2 (beta with some bug fixes)
    # 1.2.2.3 instead of 1.2-rc3 (release candidate)
    # 1.2.3.0 instead of 1.2-r (commercial distribution)
    # 1.2.3.5 instead of 1.2-r5 (commercial distribution with many bug fixes)

    expected = ['1', '1.2-a1', '1.2-b2', '1.2-r', '1.2-r5', '1.2-rc3', '1.10', '1.10-rc3', '1.11', '1.11.1', '1.11.2', '1.11.a', '1.11.b', '2.1', '2.100', '2.a', '2.b', '9.1-1', '9.1-2', '9.1-10', '9.2-1', '9.2-a', '9.2-b', '9.10-44', '9.10-45', '9.a-1', '9.a-2', '9.a-10', '9.a-20', '10.2', '10.10']

    print versions.keys()
    print json.dumps( versions, indent=4 )

    assert expected == versions.keys()
