from tools.sshlogin import Sshlogin
from tools.dev_param import dev_param
import argparse
import pprint

parser = argparse.ArgumentParser()
parser.add_argument("device_name", help="Device name to collect data")
usrip = parser.parse_args()
#print(args.device_name)

device = dev_param(usrip)

connection = Sshlogin(device[0],device[1],device[2])

memutil = connection.sendCommand('top -b -n1|grep Mem')
cpuutil = connection.sendCommand('top -b -n1|grep Cpu')

pprint.pprint(memutil)
pprint.pprint(cpuutil)