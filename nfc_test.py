import nfc
import nfc.ndef
import time
import sys

def on_connect(tag):
    print(tag)
    return True

rdwr_options = {
    'on-connect': on_connect,
}

booth_id = 'booth1'

def connect_reader(path):
    while True:
        try:
            return nfc.ContactlessFrontend(path)
        except IOError as error:
            time.sleep(0.5)
            continue

while True:
    try:
        clf = connect_reader('usb:072F:2200')
    except KeyboardInterrupt:
        sys.exit(-1)

    try:
        clf.connect(rdwr=rdwr_options)
    finally:
        clf.close()