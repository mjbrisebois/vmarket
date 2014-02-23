#!/usr/bin/python

import logging	as _log

def logging( name=None, level=None ):
    config = {
        "level":	level if level is not None else _log.DEBUG,
        "datefmt":	'%m-%d %H:%M:%S',
        "format":	'%(asctime)s.%(msecs).03d %(threadName)10.10s %(name)-15.15s %(funcName)-15.15s %(levelname)-8.8s %(message)s',
    }
    _log.basicConfig( **config )
    return _log.getLogger(name)
