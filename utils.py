from requests import get, post, put, packages
from base64 import b64encode
import ctypes

packages.urllib3.disable_warnings(packages.urllib3.exceptions.InsecureRequestWarning)

def strToB64(str):
        return b64encode(str.encode('ascii')).decode('ascii')

def checkStatusSimple(process):
        temp = subprocess.run(['wmic','PROCESS','WHERE',f'name=\'{process}\'','GET','commandline'], capture_output= True, shell = True)
        if temp.stdout.decode('utf-8').strip():
            return True
        else:
            return False

def getRequest(protocol,ip,port,endpoint,header):
    r = get(f'{protocol}://{ip}:{port}{endpoint}', headers=header,verify=False)
    return r 

def postRequest(protocol,ip,port,endpoint,data,header):
    r = post(f'{protocol}://{ip}:{port}{endpoint}', data=data,headers=header,verify=False)
    return r

def putRequest(protocol,ip,port,endpoint,data,header):
    r = put(f'{protocol}://{ip}:{port}{endpoint}', data=data,headers=header,verify=False)
    return r

def hideConsole():
            
            whnd = ctypes.windll.kernel32.GetConsoleWindow()
            if whnd != 0:
                ctypes.windll.user32.ShowWindow(whnd, 0) 