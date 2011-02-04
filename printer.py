import usb
# Alright, I don't know why pyusb1.0.0 works.
# At first it didn't, so I tried installing 0.1, then some other stuff.
# I fucking loathe everything.

busses = usb.busses()
for bus in busses:
    for device in bus.devices:
        if device.idVendor == 1659 and device.idProduct == 8963:
            print "Found the adapter."
            print "Vendor ID", device.idVendor, "(", hex(device.idVendor), ")", "Product ID", device.idProduct, "(", hex(device.idProduct), ")" 
            print "time to shit bits"
            