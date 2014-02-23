#!/usr/bin/python

import os, logging
from utils	import setup

log			= setup.logging( name=__file__ )
db_file			= 'databases/vmarket.db'

create_tables		= False
if not os.path.exists(db_file):
    # If the database doesn't already exists set flag for creating tables
    create_tables	= True

conn			= setup.db_connect(db_file)
c			= conn.cursor()

if create_tables:
    c.execute("""CREATE TABLE IF NOT EXISTS items (
              item_id		INTEGER PRIMARY KEY AUTOINCREMENT,
              seller_id		INTEGER,
              description	TEXT,
              quantity		INTEGER
          )""")


class market(object):
    
    def __init__(self, name=None):
        self.name	= name
        
    def __setitem__(self, key, value):
        """Cannot set items using market[item_id] = blah. You must use the post
        method for adding items.

        """
        pass

    def __getitem__(self, item_id):
        """market[item_id] will search the database for the item_id and return
        the result.

        """
        c.execute("SELECT * FROM items WHERE item_id = ?", (item_id,))
        return c.fetchone()

    def __delitem__(self, item_id):
        """del market[item_id] will do nothing."""
        pass

    def __iter__(self):
        c.execute("SELECT * FROM items")
        while True:
            item	= c.fetchone()
            if item is None:
                break
            yield item

    def post(self, seller_id, description=None, quantity=None):
        """Posting an item to the market.  The description message will describe
        what the seller wants for this item.

        """
        # if the table doesn't exist already we need to make it
        c.execute("INSERT INTO items (seller_id, description, quantity) VALUES (?,?,?)",
                  (seller_id, description, quantity))
        conn.commit()
        item_id		= c.lastrowid
        return item_id

    def offer(self):
        """Optionally the buyer can make an offer to the seller for something
        that may not be what the seller asked for.

        """
        pass

    def accept(self):
        """The buyer or the seller can accept the terms and an order for the
        item will be created.

        """
        pass

