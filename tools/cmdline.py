_author_ = 'Rishit Patel'
from tools.sshlogin import Sshlogin

class cmdline(Sshlogin):

    def _init_(self):
        print("this is the cmd class")
    # TODO add execute class here before adding commands
    def execute(self,command):
