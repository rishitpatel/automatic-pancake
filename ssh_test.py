import ssh
import argparse
import yaml


parser = argparse.ArgumentParser()
parser.add_argument("device_name", help="Device name to collect data")
args = parser.parse_args()
#print(args.device_name)
ip = ""
user = ""
passwd = ""
devtype = ""

def ssh_util(args):
    with open('/home/rishit/device_details/device_details.yaml') as f:
        devices =yaml.safe_load(f)
        f.close()

    device_list = list(devices.keys())

    if args not in device_list:
        print ("Device is not in the list. Please enter valid device list.")
        print("Valid Devices are:", device_list)
        return
    else:
        device_details = devices[args]

    ip = device_details['ip']
    user = device_details['username']
    passwd = device_details['password']
    devtype = device_details['type']

    return ip, user, passwd, devtype

ssh_util(args.device_name)
connection = ssh.ssh(ip, user, passwd)
connection.sendCommand('vbash -c -i "show system memory cache"')