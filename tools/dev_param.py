import yaml


def dev_param(args):
    with open('/home/rishit/device_details/device_details.yaml') as f:
        devices = yaml.safe_load(f)
        f.close()

    device_list = list(devices.keys())

    if args not in device_list:
        print("Device is not in the list. Please enter valid device list.")
        print("Valid Devices are:", device_list)
        return
    else:
        device_details = devices[args]

    ip = device_details['ip']
    user = device_details['username']
    passwd = device_details['password']
    devtype = device_details['type']

    return [ip, user, passwd, devtype]
