_author_ = 'Rishit Patel'
from tools.sshlogin import Sshlogin

class cmdline(Sshlogin):

    def _init_(self):
        print("this is the cmd class")
    # TODO add execute function here before adding commands
    def execute(self,command):
