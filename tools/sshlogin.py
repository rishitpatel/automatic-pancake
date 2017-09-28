from paramiko import client

class Sshlogin:
        client = None

        def __init__(self, address, username, password):
                print("Connecting to server.")
                self.client = client.SSHClient()
                self.client.set_missing_host_key_policy(client.AutoAddPolicy())
                self.client.connect(address, username=username, password=password, look_for_keys=False)
                self.transport = paramiko.Transport((address, 22))
                self.transport.connect(username=username, password=password)

        def sendCommand(self, command):
                if(self.client):
                        stdin, stdout, stderr = self.client.exec_command(command)
                        while not stdout.channel.exit_status_ready():
                                # Print data when available
                                if stdout.channel.recv_ready():
                                        alldata = stdout.channel.recv(1024)
                                        prevdata = b"1"
                                        while prevdata:
                                                prevdata = stdout.channel.recv(1024)
                                                alldata += prevdata

                                        return str(alldata, "utf8")
                else:
                        print("Connection not opened.")
        def close(self):
                self.client.close()

        def openSh(self):
                self.shell = self.client.()
                self.shell = self.client.invoke_shell()

## Use sendSh to send commands in Shell. Will need to open shell by
## using openSh() before sendSh()
        def sendSh(self, command):
                if(self.shell):
                        self.shell.send(command + '\n')
                else:
                        print("Shell is not open to run the command")

                if self.shell != None and self.shell.recv_ready():
                        alldata = self.shell.recv(1024)
                        while self.shell.recv_ready():
                                alldata += self.shell.recv(1024)
                        strdata = str(alldata, "utf8")
                        return strdata
                else:
                    print("Shell is not receive ready or not open")

        def outSh(self):
                if self.shell != None and self.shell.recv_ready():
                        alldata = self.shell.recv(1024)
                        while self.shell.recv_ready():
                                alldata += self.shell.recv(1024)
                        strdata = str(alldata, "utf8")
                        return strdata
                else:
                    print("Shell is not receive ready or not open")