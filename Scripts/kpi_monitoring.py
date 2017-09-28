from tools.sshlogin import Sshlogin
from tools.dev_param import dev_param
import argparse
from time import sleep

parser = argparse.ArgumentParser()
parser.add_argument("device_name", help="Device name to collect data")
args = parser.parse_args()
usrip = args.device_name
print (usrip)

device = dev_param(usrip)

connection = Sshlogin(device[0],device[1],device[2])

memutil = connection.sendCommand('')
sleep(2)
cpuutil = connection.sendCommand('')


connection.close()

print(memutil)
print(cpuutil)