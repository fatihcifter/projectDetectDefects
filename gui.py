import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from fabric import *
from PyQt5.QtCore import QObject, QThread, pyqtSignal
import time
from threading import *
class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)


class Ui_HataTespit(object):
    def setupUi(self, HataTespit):

        HataTespit.setObjectName("HataTespit")
        HataTespit.resize(1046, 798)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(HataTespit.sizePolicy().hasHeightForWidth())
        HataTespit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        HataTespit.setFont(font)
        HataTespit.setAutoFillBackground(True)
        HataTespit.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        HataTespit.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(HataTespit)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 0, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 0, 1, 1, 1)
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.page_3)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 8, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.page_3)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 2, 3, 1, 1)
        self.photo = QtWidgets.QLabel(self.page_3)
        self.photo.setStyleSheet("background-color: white;\n"
                                   "    border-style: outset;\n"
                                   "    border-width: 2px;\n"
                                   "    border-radius: 10px;\n"
                                   "    border-color: beige;\n"
                                   "    font: bold 14px;\n"
                                   "    min-width: 10em;\n"
                                   "    margin: 25px;\n"
                                   "    padding: 6px;")
        self.photo.setText("")
        self.photo.setPixmap(QtGui.QPixmap("../../Downloads/untitled/Ekran Alıntısı.JPG"))
        self.photo.setScaledContents(True)
        self.photo.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.photo, 1, 0, 7, 3)
        self.pushButton_2 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
                                        "    background-color: rgb(30, 255, 135);    \n"
                                        "    border-style: outset;\n"
                                        "    border-width: 2px;\n"
                                        "    border-radius: 10px;\n"
                                        "    border-color: beige;\n"
                                        "    font: bold 14px;\n"
                                        "    min-width: 10em;\n"
                                        "    padding: 6px;\n"
                                        "}\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color: rgb(46, 255, 196);\n"
                                        "    border-style: inset;\n"
                                        "}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 8, 3, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 8, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.page_3)
        self.pushButton.setStyleSheet("QPushButton {\n"
                                      "    background-color: rgb(255, 24, 74);    \n"
                                      "    border-style: outset;\n"
                                      "    border-width: 2px;\n"
                                      "    border-radius: 10px;\n"
                                      "    border-color: beige;\n"
                                      "    font: bold 14px;\n"
                                      "    min-width: 10em;\n"
                                      "    padding: 6px;\n"
                                      "}\n"
                                      "QPushButton:pressed {\n"
                                      "    background-color: rgb(255, 58, 78);\n"
                                      "    border-style: inset;\n"
                                      "}")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 9, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.page_3)
        self.label_2.setAutoFillBackground(True)
        self.label_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 9, 0, 1, 3)
        self.pushButton_4 = QtWidgets.QPushButton(self.page_3)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_2.addWidget(self.pushButton_4, 8, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.page_3)
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: white;\n"
                                 "    border-style: outset;\n"
                                 "    border-width: 2px;\n"
                                 "    border-radius: 10px;\n"
                                 "    border-color: beige;\n"
                                 "    font: bold 14px;\n"
                                 "    min-width: 10em;\n"
                                 "    padding: 6px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 3, 3, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.page_3)
        self.label_3.setMinimumSize(QtCore.QSize(186, 85))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: White;\n"
                                   "    border-style: outset;\n"
                                   "    border-width: 2px;\n"
                                   "    border-radius: 10px;\n"
                                   "    border-color: beige;\n"
                                   "    font: bold 14px;\n"
                                   "    min-width: 10em;\n"
                                   "    padding: 6px;")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 5, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.page_3)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 4, 3, 1, 1)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_8 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_8.setStyleSheet("QPushButton {\n"
                                        "    background-color: rgb(255, 24, 74);    \n"
                                        "    border-style: outset;\n"
                                        "    border-width: 2px;\n"
                                        "    border-radius: 10px;\n"
                                        "    border-color: beige;\n"
                                        "    font: bold 14px;\n"
                                        "    min-width: 10em;\n"
                                        "    padding: 6px;\n"
                                        "}\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color: rgb(255, 58, 78);\n"
                                        "    border-style: inset;\n"
                                        "}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout_3.addWidget(self.pushButton_8, 2, 2, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_7.setStyleSheet("QPushButton {\n"
                                        "    background-color: rgb(255, 24, 74);    \n"
                                        "    border-style: outset;\n"
                                        "    border-width: 2px;\n"
                                        "    border-radius: 10px;\n"
                                        "    border-color: beige;\n"
                                        "    font: bold 14px;\n"
                                        "    min-width: 10em;\n"
                                        "    padding: 6px;\n"
                                        "}\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color: rgb(255, 58, 78);\n"
                                        "    border-style: inset;\n"
                                        "}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout_3.addWidget(self.pushButton_7, 3, 2, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.page_4)
        self.textEdit.setEnabled(True)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_3.addWidget(self.textEdit, 0, 0, 1, 3)
        self.label_14 = QtWidgets.QLabel(self.page_4)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 3, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.page_4)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 2, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.page_4)
        self.label_11.setAutoFillBackground(True)
        self.label_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_11.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 2, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.page_4)
        self.label_9.setAutoFillBackground(True)
        self.label_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_9.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 3, 1, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_9.setStyleSheet("QPushButton{\n"
                                        "    background-color: rgb(30, 255, 135);    \n"
                                        "    border-style: outset;\n"
                                        "    border-width: 2px;\n"
                                        "    border-radius: 10px;\n"
                                        "    border-color: beige;\n"
                                        "    font: bold 14px;\n"
                                        "    min-width: 10em;\n"
                                        "    padding: 6px;\n"
                                        "}\n"
                                        "QPushButton:pressed {\n"
                                        "    background-color: rgb(46, 255, 196);\n"
                                        "    border-style: inset;\n"
                                        "}")
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout_3.addWidget(self.pushButton_9, 1, 1, 1, 1)
        self.stackedWidget.addWidget(self.page_4)
        self.gridLayout.addWidget(self.stackedWidget, 4, 0, 1, 3)
        HataTespit.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(HataTespit)
        self.statusbar.setObjectName("statusbar")
        HataTespit.setStatusBar(self.statusbar)

        self.retranslateUi(HataTespit)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(HataTespit)

    def retranslateUi(self, HataTespit):
        _translate = QtCore.QCoreApplication.translate
        HataTespit.setWindowTitle(_translate("HataTespit", "Hata Tespit"))
        self.pushButton_6.setText(_translate("HataTespit", "Hata Tespit Sayfası"))
        self.pushButton_5.setText(_translate("HataTespit", "Hata Eğitim"))
        self.label_4.setText(_translate("HataTespit", "Dosya Adı"))
        self.label_7.setText(_translate("HataTespit", "Kumaş Hatalı Mı ?"))
        self.pushButton_2.setText(_translate("HataTespit", "Test Et"))
        self.pushButton_3.setText(_translate("HataTespit", "İleri"))
        self.pushButton.setText(_translate("HataTespit", "Dosya Seç"))
        self.label_2.setText(_translate("HataTespit", "Dosya Yolu"))
        self.pushButton_4.setText(_translate("HataTespit", "Geri"))
        self.label.setText(_translate("HataTespit", "Kumaş Hata Tespiti"))
        self.label_3.setText(_translate("HataTespit", "Pred"))
        self.label_6.setText(_translate("HataTespit", "Tahmini Değer"))
        self.pushButton_8.setText(_translate("HataTespit", "Dosya Seç"))
        self.pushButton_7.setText(_translate("HataTespit", "Dosya Seç"))
        self.label_14.setText(_translate("HataTespit", "DataTest"))
        self.label_12.setText(_translate("HataTespit", "DataSet"))
        self.label_11.setText(_translate("HataTespit", "Dosya Yolu"))
        self.label_9.setText(_translate("HataTespit", "Dosya Yolu"))
        self.pushButton_9.setText(_translate("HataTespit", "Eğitimi Başlat"))
        self.pushButton.clicked.connect(self.pushButton_handler)
        self.pushButton_2.clicked.connect(self.pushButton_2_handler)
        self.pushButton_3.clicked.connect(self.pushButton_3_handler)
        self.pushButton_4.clicked.connect(self.pushButton_4_handler)
        self.pushButton_7.clicked.connect(self.pushButton_7_handler)
        self.pushButton_8.clicked.connect(self.pushButton_8_handler)
        self.pushButton_9.clicked.connect(self.pushButton_9_handler)
        ## page 1
        self.pushButton_6.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_3))
        ## page 2
        self.pushButton_5.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_4))

    def setboxes(self,path,b) :
        self.photo.setPixmap(QtGui.QPixmap(path+imgtested[b][0]))
        self.label.setText(imgtested[b][2])
        self.label_3.setText("%"+str(100*float(('%.2f' % imgtested[b][1]))))



    def pushButton_handler(self):
        path = self.select_folder()
        self.label_2.setText(path)

    def pushButton_7_handler(self):
        path = self.select_folder()
        self.label_9.setText(path)
    def pushButton_8_handler(self):
        path = self.select_folder()
        self.label_11.setText(path)
    def pushButton_9_handler(self):
        self.textEdit.setText("Eğitim Başlıyor lütfen bekleyin...")
        t1=Thread(target=self.Operation)
        t1.start()
        self.textEdit.show()

    def Operation(self):
        print("time start")
        dataSetTrain= self.label_11.text()
        dataSetTest= self.label_9.text()
        runTrainTest(dataSetTrain, dataSetTest)
        print("time startsada")

    def pushButton_2_handler(self):
        path = self.label_2.text()
        global a
        a = path.replace('/', '\\')+"\\"
        global imgtested
        imgtested = test_et(a)
        global counter
        counter = len(imgtested) - 1
        self.label_4.setText("0")
        self.setboxes(a,0)



    def select_folder(self):
        path = QFileDialog.getExistingDirectory()
        return path


    def pushButton_3_handler(self):
        x=int(self.label_4.text())
        print(x)
        if counter > x :
            x += 1
            self.setboxes(a,x)
            self.label_4.setText(str(x))


    def pushButton_4_handler(self):
        x=int(self.label_4.text())
        if x > 0:
            x -= 1
            pathp= a+imgtested[x][0]
            self.setboxes(a,x)
            self.label_4.setText(str(x))
        if x == 0:
            self.setboxes(a,x)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HataTespit = QtWidgets.QMainWindow()
    ui = Ui_HataTespit()
    ui.setupUi(HataTespit)
    HataTespit.show()
    sys.exit(app.exec_())
