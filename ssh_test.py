import ssh
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("device_name", help="Device name to collect data")
args = parser.parse_args()
print(args)
connection = ssh.ssh("ip", "rishit", "pw")
connection.sendCommand('vbash -c -i "show system memory cache"')