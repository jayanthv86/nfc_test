import nfc
import nfc.ndef
import time
import sys
import ast
import csv
import json
connected = False

def on_connect(tag):
    print(tag)
    if tag.ndef:
        record_1 = tag.ndef.message[0]
        smartposter = nfc.ndef.SmartPosterRecord(record_1)
        title = smartposter.title
	csv_record = title.get('en').encode('utf-8')
	csv_record = csv_record.replace("u'", "'")
	print(csv_record)
        print(type(ast.literal_eval(csv_record)))
        mydict = ast.literal_eval(csv_record)
	print(mydict)
        
        f = open('mycsvfile.csv', 'w')  # Just use 'w' mode in 3.x
        w = csv.DictWriter(f, mydict.keys())
        w.writeheader()
        w.writerow(mydict)

    time.sleep(5)
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
        if not connected:
            clf = connect_reader('usb:072F:2200')
            connected = True
    except KeyboardInterrupt:
        sys.exit(-1)

    clf.connect(rdwr=rdwr_options)
