from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication,QDialog
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import youtube_dl
import sys
import os


audon = {
    'format' : 'bestaudio'
}
vna = {
    'preferedquality' : '22'
}
vdoon = {
    'format' : 'bestvideo'
}

class aps(QDialog):
    def __init__(self):
        super(aps,self).__init__()
        cd = os.getcwd()
        loadUi('final.ui',self)
        self.setWindowTitle('BK YT Downloader')
        self.videobtn.clicked.connect(self.bestvideo)
        self.audiobtn.clicked.connect(self.bestaudio)
        self.videoonlybtn.clicked.connect(self.videoonly)
        self.selectbtn.clicked.connect(self.selectdir)
        self.directory.setText('Please provide the link of the youtube video and \n select the type of media you want to download')
        self.fold.setText('Select a directory')
    def selectdir(self):
        global pathdir
        pathdir = str(QFileDialog.getExistingDirectory())
        os.chdir(pathdir)
        self.fold.setText(pathdir)

    def bestvideo(self):
        self.url = self.vidurl.text()
        if self.url == '':
            self.directory.setText("You have not provided any link.\n Please provide the link and try again")
        else:
            self.directory.setText('Video has been downloaded')
        try:
            with youtube_dl.YoutubeDL(vna) as ydl:
                ydl.download([self.url])
        except:
            pass

    def bestaudio(self):
        self.url = self.vidurl.text()
        if self.url == '':
            self.directory.setText("You have not provided any link.\n Please provide the link and try again")
        else:
            self.directory.setText('Audio has been downloaded')
        try:
            with youtube_dl.YoutubeDL(audon) as ydl:
                ydl.download([self.url])
        except:
            pass

    def videoonly(self):
        self.url = self.vidurl.text()
        if self.url == '':
            self.directory.setText("You have not provided any link.\n Please provide the link and try again")
        else:
            self.directory.setText('Video has been downloaded without the video')
        try:
            with youtube_dl.YoutubeDL(vdoon) as ydl:
                ydl.download([self.url])
        except:
            pass


app = QApplication(sys.argv)
widget = aps()
widget.show()
sys.exit(app.exec_())
