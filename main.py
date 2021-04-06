from sys import argv, exit
from PySide2.QtWidgets import QApplication, QMainWindow, QMessageBox 
from PySide2.QtCore import Qt, QPoint
from PySide2.QtGui import QIcon
from poorLCU import LCU 
from json import dumps, loads, load, dump 

import subprocess
from socket import gethostbyname

from ui_main import Ui_MainWindow
import os
import ctypes
from utils import getRequest,putRequest,postRequest,checkStatusSimple, strToB64, hideConsole
import logging


hideConsole()

class MainWindow(QMainWindow):

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        if(self.ui.top_bar.underMouse()):
            delta = QPoint (event.globalPos() - self.oldPos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #MainWindow
        self.setWindowFlag(Qt.FramelessWindowHint)
        #MainWindow
        self.setAttribute(Qt.WA_TranslucentBackground)


        self.ui.stackedWidget.setCurrentIndex(0)

        
        self.ui.spinQueue.setCurrentIndex(0)
                

        self.show()
        
        
        self.lcu = LCU()
        self.settings = self.lcu.connect()
        if(not self.settings):
            self.showPopup('Please start League','League is not running','Icon.ico')
            exit(-1)
        self.auth = strToB64('riot:{}'.format(self.settings['auth']))
        self.header = {'Accept': 'application/json', 'Authorization': f'Basic {self.auth}'}

        

        

        
        # ComboBox(Spinners) Setup
        #Division
        for i in ['Select a Queue','RANKED_SOLO_5x5','RANKED_TFT','RANKED_TEAM_5x5']:
            self.ui.spinQueue.addItem(i)
        self.ui.spinQueue.setCurrentIndex(0)
        
        for i in ['Select a Tier','IRON','BRONZE','SILVER','GOLD','PLATINUM','DIAMOND','MASTER','GRANDMASTER','CHALLENGER']:
            self.ui.spinTier.addItem(i)
        self.ui.spinTier.setCurrentIndex(0)

        for i in['Select a Division','I','II','III','IV']:
            self.ui.spinDiv.addItem(i)
        self.ui.spinDiv.setCurrentIndex(0)

        #Icons
        for i in ['Select an Icon Code','29','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78']:
            self.ui.spinIC.addItem(i)
        self.ui.spinIC.setCurrentIndex(0)

        #Methods
        for i in ['Method','GET','POST','PUT']:
            self.ui.spinnerMethod.addItem(i)
        self.ui.spinnerMethod.setCurrentIndex(0)
        self.ui.spinnerMethod.currentIndexChanged.connect(self.spinMethodChanged)

        
        #Colour btnOffline based on file
        if self._checkOffline():
            # ON
            self.ui.btnOffline.setText('Offline Status [ON]')
            self.ui.btnOffline.setStyleSheet('background-color: #20ff5f;')
        else:
            # OFF
            self.ui.btnOffline.setText('Offline Status [OFF]')
            self.ui.btnOffline.setStyleSheet('background-color: #ff1a29;')

    def hideConsole(self):
        whnd = ctypes.windll.kernel32.GetConsoleWindow()
        if whnd != 0:
            ctypes.windll.user32.ShowWindow(whnd, 0)

        

        # Buttons to navigate
        self.ui.gotoPage2.clicked.connect(self.gotoPage2)
        self.ui.gotoPage1.clicked.connect(self.gotoPage1)
        self.ui.gotoAdvanced.clicked.connect(self.gotoAdvanced)

        # Buttons Clicks
        self.ui.btnIC.clicked.connect(self.setIcon)
        self.ui.btnCIC.clicked.connect(self.setCustomIcon)
        self.ui.btnStatus.clicked.connect(self.setStatus)
        self.ui.btnBg.clicked.connect(self.setBg)

        self.ui.btnDiv.clicked.connect(self.setDivision)
    

        self.ui.btnOffline.clicked.connect(self.setOffline)

        self.ui.btnSend.clicked.connect(self.sendRequest)





        #Menu Buttons
        self.ui.btnMinimize.clicked.connect(lambda: self.showMinimized())
        self.ui.btnClose.clicked.connect(lambda: self.close())

      

    # Icons window functions
    def setIcon(self):
        if(self.ui.spinIC.currentIndex() != 0):
            end = '/lol-summoner/v1/current-summoner/icon/'
            data = {"profileIconId": self.ui.spinIC.currentText()}
            putRequest(self.settings['protocol'],'127.0.0.1',self.settings['port'],end,dumps(data),self.header)

    def setCustomIcon(self):
        end = "/lol-chat/v1/me/"
        data = {"icon": self.ui.txtCIC.text()}
        putRequest(self.settings['protocol'],'127.0.0.1',self.settings['port'],end,dumps(data),self.header)

    # Division window functions
    def setDivision(self):
        if(self.ui.spinQueue.currentIndex() != 0 and self.ui.spinTier.currentIndex() != 0 and self.ui.spinDiv.currentIndex() != 0 ):
            end = "/lol-chat/v1/me/"
            data = {
                "lol": {
                    "rankedLeagueQueue": f'{self.ui.spinQueue.currentText()}',
                    "rankedLeagueTier": f'{self.ui.spinTier.currentText()}',
                    "rankedLeagueDivision": f'{self.ui.spinDiv.currentText()}',
                },
            }
            putRequest(self.settings['protocol'],'127.0.0.1',self.settings['port'],end,dumps(data),self.header)

    # Status window functions
    def setStatus(self):
        end = '/lol-chat/v1/me/'
        data = {"statusMessage": f'{self.ui.txtStatus.toPlainText()}' }
        putRequest(self.settings['protocol'],'127.0.0.1',self.settings['port'],end,dumps(data,ensure_ascii=False).encode('utf-8'),self.header)

    # Background window functions
    def setBg(self):
        end = '/lol-summoner/v1/current-summoner/summoner-profile/'
        data = {
            'key': "backgroundSkinId",
            'value': self.ui.txtBg.text(),
        }
        postRequest(self.settings['protocol'],'127.0.0.1',self.settings['port'],end,dumps(data),self.header)


    def _checkOffline(self,file='settings.json'):
        f = open(file,'r')
        data = load(f)
        f.close()
        return data['settings']['chatBlocked'] #1 On | #0 Off



    def setOffline(self):
        try:
            is_admin = os.getuid() == 0
        except AttributeError:
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

        if(not is_admin):
            self.showPopup('To create a firewall rule i need admin privileges.','Please run the program as Administrator','Icon.ico')   
            return -1



        end = '/riotclient/get_region_locale' 
        with open('settings.json','r') as f:
            data = load(f)
        
        if(data['settings']['chatBlocked']): # == 1
            subprocess.run(['netsh','advfirewall','firewall','delete','rule','name=\"lolchat\"'])
            data['settings']['chatBlocked'] = 0
            self.ui.btnOffline.setText('Offline Status [OFF]')
            self.ui.btnOffline.setStyleSheet('background-color: #ff1a29;')
        else: 
            hosts = {
                'EUW':'euw1.chat.si.riotgames.com',
                'EUNE':'eun1.chat.si.riotgames.com',
                'BR':'br.chat.si.riotgames.com',
                'NA':'na2.chat.si.riotgames.com',
                'LAN':'la1.chat.si.riotgames.com',
                'LAS':'la2.chat.si.riotgames.com',
                'TR':'tr1.chat.si.riotgames.com',
                'RU':'ru1.chat.si.riotgames.com',  
                'JP':'jp1.chat.si.riotgames.com',
                'OCE':'oc1.chat.si.riotgames.com',
                'VN':'vn1.chat.si.riotgames.com',
                'PH':'ph1.chat.si.riotgames.com',
                'SG':'sg1.chat.si.riotgames.com',
                'TH':'th1.chat.si.riotgames.com',
                'TW':'tw1.chat.si.riotgames.com',
                
            }

            rec = getRequest(self.settings['protocol'],'127.0.0.1',self.settings['port'],end, self.header) 
            subprocess.run(['netsh','advfirewall','firewall','add','rule','name=\"lolchat\"','dir=out','remoteip={}'.format(gethostbyname(hosts[rec.json()['region']])),'protocol=TCP','action=block'], shell = True)
            data['settings']['chatBlocked'] = 1
            self.ui.btnOffline.setText('Offline Status [ON]')
            self.ui.btnOffline.setStyleSheet('background-color: #20ff5f;')

        with open('settings.json','w') as f:
            dump(data,f)

    #Advanced
    def sendRequest(self):
        method = self.ui.spinnerMethod.currentText()
        end = self.ui.txtEndpoint.text()
        if(method == 'GET'):
            resp = getRequest(self.settings['protocol'],'127.0.0.1',self.settings['port'],end,self.header) 
        else:
            data = self.ui.txtData.toPlainText()
            if(method == 'POST'):
                resp = postRequest(self.settings['protocol'],'127.0.0.1',self.settings['port'],end,dumps(loads(data)),self.header)
            else: #PUT Request
                resp = putRequest(self.settings['protocol'],'127.0.0.1',self.settings['port'],end,dumps(loads(data)),self.header)

        self.ui.txtResp.setPlainText(dumps(resp.json()))
        self.ui.txtCode.setText(str(resp.status_code))



    # GOTO functions
    def gotoPage1(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def gotoPage2(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def gotoAdvanced(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def spinMethodChanged(self):
        if self.ui.spinnerMethod.currentIndex()==1:
            self.ui.txtData.setVisible(False)
        else:
            self.ui.txtData.setVisible(True)



    # Popup
    def showPopup(self,text,infoText,pathToIcon):
        p = QMessageBox()
        p.setIcon(QMessageBox.Critical)
        p.setText(text)
        p.setInformativeText(infoText)
        p.setWindowIcon(QIcon(pathToIcon))

        p.exec_()



            
if __name__ == "__main__":
    app = QApplication(argv)
    
    window = MainWindow()

    exit(app.exec_())
