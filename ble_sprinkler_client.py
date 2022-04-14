from bluepy.btle import Scanner, DefaultDelegate, Peripheral

class ScanDelegate(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleDiscovery(self, dev, isNewDev, isNewData):
        if isNewDev:
            print("Discovered device", dev.addr)
            # the below is the one that I'm looking for
            if "b8:27:eb:d4:6a:e6" == dev.addr:
                p = Peripheral()
                p.connect("B8:27:EB:D4:6A:E6")
                for svc in p.getServices():
                    print(" service %s uuid %s"%(str(svc), str(svc.uuid)))
                    chars = svc.getCharacteristics()
                    for c in chars:
                        print("  Chara %s %s props %s"%(c.getHandle(),str(c.uuid), c.propertiesToString()))
                        if str(c.uuid) == "2AFB":
                            p.writeCharacteristic(c.getHandle(), "ON".encode("utf-8"), True)


            
        elif isNewData:
            print("Received new data from", dev.addr)

scanner = Scanner().withDelegate(ScanDelegate())
devices = scanner.scan(10.0)

for dev in devices:
    print("Device %s (%s), RSSI=%d dB" % (dev.addr, dev.addrType, dev.rssi))
    for (adtype, desc, value) in dev.getScanData():
        print("  %s = %s" % (desc, value))

