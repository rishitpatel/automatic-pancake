import ssh
import argparse
import yaml


parser = argparse.ArgumentParser()
parser.add_argument("device_name", help="Device name to collect data")
args = parser.parse_args()
print(args)

with open('/home/rishit/device_details/device_details.yaml') as f:
    devices =yaml.safe_load(f)
    f.close()

device_list = devices.keys()

if args not in device_list:
    print ("Device is not in the list. Please enter valid device list.")
    return
else:
    device_details = devices[args]

ip = device_details['ip']
user = device_details['username']
passwd = device_details['password']
devtype = device_details['type']

print(ip,user,passwd,devtype)

#connection = ssh.ssh("ip", "rishit", "pw")
#connection.sendCommand('vbash -c -i "show system memory cache"')