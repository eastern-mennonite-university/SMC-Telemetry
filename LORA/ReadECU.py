import hid

def read_ecu():
    ecu = hid.Device(22616, 6)
    print(ecu)
    print('no device')

    while True:
        data = ecu.read(41)
        print(data)

read_ecu()
