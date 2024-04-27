
from digi.xbee.devices import XBeeDevice
from digi.xbee.exception import TimeoutException
import time 
PORT = "COM18"
BAUD_RATE = 9600
MACIDs = dict(
    { "0013A200423F63E6": "MAKARA" ,
    "0013A200423F63DC": "KURMA" ,
    "0013A200423F63D8" : "COMMAND"}
)
    
def main():
    device = XBeeDevice(PORT, BAUD_RATE)
    device.open(force_settings=True)
    devid = device.get_node_id()
    devrole = device.get_role()
    device.set_sync_ops_timeout(6)
    print(" +-----------------------------------------------------------------------+")
    print(f" | XBee ID: {devid} | PORT: {PORT} | BAUD: {BAUD_RATE}| ROLE : {devrole}")
    print(" +-----------------------------------------------------------------------+\n")

    try:
        

        def data_receive_callback(xbee_message):
            remoteaddr = xbee_message.remote_device.get_64bit_addr()
            remoteid = MACIDs[str(remoteaddr)]
            print(" %s >> %s" % (remoteid,
                                     xbee_message.data.decode()))
        while True:
            try:
                device.add_data_received_callback(data_receive_callback)
                time.sleep(0.2)
                print("Waiting for data...\n")
                try:
                    broadcastmsg = f"KURMA,LAT{202324242},LON{142526262},SOG{252},COG{122},Heading{232}"
                    device.send_data_broadcast(f"{broadcastmsg}",8)
                except TimeoutException:
                    print("Broadcast timeout occurred for Device . Retrying...")
                # print(device.get_sync_ops_timeout())
                time.sleep(0.2)
                print("Info broadcasted ..")
            except KeyboardInterrupt:
                print("\nKeyboard interruption detected. Exiting...")
                break
    finally:
        if device is not None and device.is_open():
            device.close()

if __name__ == '__main__':
    main()