#!/usr/bin/python

from collections import OrderedDict

class Version(OrderedDict):
    
    def __init__( self ):
        super(Version, self).__init__()

    def __setitem__( self, name, value ):
        super(Version, self).__setitem__( name, value )
        self.sort()

    def sort( self ):
        keys		= self.keys()
        def k(v):
            if v.isdigit():
                return int(v)
            else:
                try:
                    # v and r could both be either a int or a str at this point.
                    v,r	= v.split('-', 2)
                    if not v.isdigit():
                        v		= str(ord(v))
                    v		       += "."
                    if r.isdigit():
                        v	       += "%05d" % int(r)
                    else:
                        for i in r:
                            if i.isdigit():
                                n	= int(i)
                            else:
                                n	= ord(i)
                            v      += "%05d" % n
                    v	= float(v)
                except Exception as exc:
                    pass
                return v
        keys.sort( key=lambda s: map(k, s.split('.')) )
        for k in keys:
            v		= self[k]
            del self[k]
            super(Version, self).__setitem__( k, v )
        