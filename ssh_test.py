import ssh

connection = ssh.ssh("ip", "rishit", "pw")
connectin.sendCommand('vbash -c -i "show system memory cache"')