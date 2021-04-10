from requests import get, post, put, packages
from requests.exceptions import ConnectionError
from base64 import b64encode
import ctypes
from os.path import exists
import json
import sys

_title = 'Connection refused'
_desc = 'Please open League and restart the program'
_icon = 'Icon.ico'

def strToB64(str):
        return b64encode(str.encode('ascii')).decode('ascii')

def checkStatusSimple(process):
        temp = subprocess.run(['wmic','PROCESS','WHERE',f'name=\'{process}\'','GET','commandline'], capture_output= True, shell = True)
        if temp.stdout.decode('utf-8').strip():
            return True
        else:
            return False

def getRequest(protocol,ip,port,endpoint,header,func=lambda a,b,c: None):
    try:
        r = get(f'{protocol}://{ip}:{port}{endpoint}', headers=header,verify=False)
        return r 
    except ConnectionError:
        func(_title,_desc,_icon)
        sys.exit(-1)


def postRequest(protocol,ip,port,endpoint,data,header):
    try:
        r = post(f'{protocol}://{ip}:{port}{endpoint}', data=data,headers=header,verify=False)
        return r
    except ConnectionError:
        func(_title,_desc,_icon)
        sys.exit(-1)

def putRequest(protocol,ip,port,endpoint,data,header):
    try:
        r = put(f'{protocol}://{ip}:{port}{endpoint}', data=data,headers=header,verify=False)
        return r
    except ConnectionError:
        func(_title,_desc,_icon)
        sys.exit(-1)

def writeFileIfNotExists(name,dataJson):
    if not exists(name):
        f = open(name,'w')
        json.dump(dataJson,f)
        f.close()







