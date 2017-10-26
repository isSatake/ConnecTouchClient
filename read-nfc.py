import nfc
import binascii
import requests
from datetime import datetime

readerId = 22

def startup(targets):
    print 'waiting for NFC tag ...'
    return targets

def connected(tag):
    id = binascii.hexlify(tag.identifier)
    date = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    print("|%s| %s" % (date, id))
    params = {'nfcId': id, 'readerId': readerId}
    res = requests.get('http://localhost:8000', params=params)
    print(res.text)
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
