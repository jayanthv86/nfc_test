__author__ = 'roymu_000'
import nfc
import nfc.ndef
import time
import uuid

def on_connect(tag):
    print(tag)


rdwr_options = {
    'on-connect': on_connect,
}

def write_tag(tag, tag_uid):
    if tag.ndef:
        sp = nfc.ndef.SmartPosterRecord("http://nfcpy.org", tag_uid, action="save")
        print(sp.title)
        tag.ndef.message = nfc.ndef.Message(sp)
        return True

def main():
    with nfc.ContactlessFrontend('usb:072F:2200') as clf:
        while 1:
            tag = clf.connect(rdwr=rdwr_options)
            uuid_str = uuid.uuid1()
            if write_tag(tag, uuid_str):
                print("Written")
                time.sleep(5)

if __name__ == '__main__':
    main()
