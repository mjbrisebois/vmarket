#!/usr/bin/python

import logging	as _log
import sqlite3	as sql

def logging( name=None, level=None ):
    if level:
        config = {
            "level":	level if level is not None else _log.DEBUG,
            "datefmt":	'%m-%d %H:%M:%S',
            "format":	'%(asctime)s.%(msecs).03d %(threadName)10.10s %(name)-15.15s %(funcName)-15.15s %(levelname)-8.8s %(message)s',
        }
        _log.basicConfig( **config )
    return _log.getLogger(name)

def db_connect( db ):
    def dict_factory(cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]]	= row[idx]
        return d
    conn		= sql.connect(db)
    conn.row_factory	= dict_factory    
    return conn