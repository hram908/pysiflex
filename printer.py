#!/usr/bin/python

import usb
# Alright, I don't know why pyusb1.0.0 works.
# At first it didn't, so I tried installing 0.1, then some other stuff.
# I fucking loathe everything.

# rfc2217 ?

baudrate = 9600
posiflex = None

# This'll print 01234567, I think.
data = [0x1F, 0x01, 0x0D, 0x30, 0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38, 0x39, 0x30, 0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37]
# This is the string
string = ''.join([chr(x) for x in data])

#busses = usb.busses()
#for bus in busses:
#    for device in bus.devices:
#        if device.idVendor == 1659 and device.idProduct == 8963:
#            print "Found the adapter."
#            print "Vendor ID", device.idVendor, "(", hex(device.idVendor), ")", "Product ID", device.idProduct, "(", hex(device.idProduct), ")" 
#            print "time to shit bits"
#            posiflex = device
#            break

try:
    posiflex = usb.Device( usb.core.find(idVendor=1659, idProduct=8963) )
    print "Vendor ID", posiflex.idVendor, "(", hex(posiflex.idVendor), ")", "Product ID", posiflex.idProduct, "(", hex(posiflex.idProduct), ")" 
except:
    posiflex = None
    print "None found."

if posiflex is not None:
    print "Writing..."
    handle = posiflex.open()
    handle.claimInterface(0)
    handle.bulkWrite(02, string, 1000)
    handle.releaseInterface()