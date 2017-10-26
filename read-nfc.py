# -*- coding: utf-8 -*-

import nfc
import binascii
import requests
from datetime import datetime
from uuid import getnode as get_mac

readerId = get_mac() #48bit integer

def startup(targets):
    print 'waiting for NFC tag ...'
    return targets

def connected(tag):
    id = binascii.hexlify(tag.identifier)
    date = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    print("|%s| readerId: %s nfcId: %s" % (date, readerId, id))
    params = {'nfcId': id, 'readerId': readerId}
    try:
        res = requests.get('http://connectouch.org/', params=params)
        print(res.text)
    except Exception, e:
        print(e)
    return id

def released(tag):
    return('released')

clf = nfc.ContactlessFrontend('usb')
if clf:
    while clf.connect(rdwr={
        'on-startup': startup,
        'on-connect': connected,
        'on-release': released,
    }):
      pass
