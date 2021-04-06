import subprocess
import re

class LCU:
    def __init__(self):
        self.path = ""
        self.pid = 0
        self.port = 0
        self.auth = None
        self.protocol = None
        self.name = None

    def connect(self):
        inLogin = self.getPathFromExe()
        
        try:
            f = open(self.path+r'\lockfile','r')
        except:
            return False

        self.name,self.pid,self.port,self.auth,self.protocol = f.readline().split(':')
        f.close()
        return {
            'protocol': self.protocol,
            'port': self.port,
            'auth': self.auth
        }

    def checkStatus(self,process):
        temp = subprocess.run(['wmic','PROCESS','WHERE',f'name=\'{process}\'','GET','commandline'], capture_output= True, shell = True)
        if temp.stdout.decode('utf-8').strip():
            b = re.search(r"[^\"](.*exe)",temp.stdout.decode('utf-8')).group(1)[1::].split('/')
            self.path = f'{b[0]}/{b[1]}/League of Legends'
            self.port = re.search(r"--app-port=([0-9]*)",temp.stdout.decode('utf-8')).group(1)
            self.auth = re.search(r'--remoting-auth-token=(\S+)',temp.stdout.decode('utf-8')).group(1)
            return True
        else:
            return False

    def getPathFromExe(self):
        temp = self.checkStatus('RiotClientUx.exe')
        if(temp is not False):
            return True #Login
        temp = self.checkStatus('leagueClientUx.exe')
        if(temp is not False):
            return False #sClient


        
       
