from digi.xbee.devices import XBeeDevice, RemoteXBeeDevice, XBee64BitAddress
gs_command = "CMD,2016,ST,13:35:59"

#GS XBEE
device = XBeeDevice("COM10", 9600)
device.open()

#Remote XBEE payload
remote = RemoteXBeeDevice(device, XBee64BitAddress.from_hex_string("0013A200423E94A8"))

def send_command(command):
    device.send_data(remote, command)

xbee_message = device.read_data(10000)
print(xbee_message.data.decode("utf8"))
send_command(gs_command)

if device is not None and device.is_open():
    device.close()