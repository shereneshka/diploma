import numpy as np
from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets

class Dialog(QtWidgets.QDialog):
    def __init__(self, parent=None):                      # + parent
        super(Dialog, self).__init__(parent)            #
        self.parent = parent                              #

        self.setWindowTitle('Параметры субкадра')
        self.setModal(True)
        self.head = QtWidgets.QLabel('<html><b>Пожалуйста, введите в имитатор следующие параметры:</b></html>')
        self.frames = QtWidgets.QTextBrowser()
        self.frames.setFixedSize(100,30)
        self.dtime = QtWidgets.QTextBrowser()
        self.dtime.setFixedSize(100,30)
        self.dnoise = QtWidgets.QTextBrowser()
        self.dnoise.setFixedSize(100,30)
        self.dVx = QtWidgets.QTextBrowser()
        self.dVx.setFixedSize(100, 30)
        self.dVy = QtWidgets.QTextBrowser()
        self.dVy.setFixedSize(100,30)
        self.ready = QtWidgets.QPushButton("Готово")

        self.ready.clicked.connect(self.closeDialog)

        self.form = QtWidgets.QFormLayout()
        self.form.setSpacing(20)

        self.form.addRow(self.head)
        self.form.addRow("&Количество субкадров:", self.frames)
        self.form.addRow("&Время экспозиции субкадра, мс:", self.dtime)
        self.form.addRow("&Шум субкадра, эл/выб:", self.dnoise)
        self.form.addRow("&Скорость субкадра по горизонтали, пикс/кадр:", self.dVx)
        self.form.addRow("&Скорость субкадра по вертикали, пикс/кадр:", self.dVy)
        self.form.addRow(self.ready)

        self.setLayout(self.form)

    def closeDialog(self):
        self.close()


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        MainWindow.resize(737, 527)
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(24, 20, 691, 461))
        self.tab = QtWidgets.QWidget()
        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setGeometry(QtCore.QRect(90, 50, 261, 291))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.Vx_label = QtWidgets.QLabel(self.widget)
        self.verticalLayout.addWidget(self.Vx_label)
        self.Vy_label = QtWidgets.QLabel(self.widget)
        self.verticalLayout.addWidget(self.Vy_label)
        self.time_label = QtWidgets.QLabel(self.widget)
        self.verticalLayout.addWidget(self.time_label)
        self.noise_label = QtWidgets.QLabel(self.widget)
        self.verticalLayout.addWidget(self.noise_label)
        self.shift_label = QtWidgets.QLabel(self.widget)
        self.verticalLayout.addWidget(self.shift_label)
        self.widget1 = QtWidgets.QWidget(self.tab)
        self.widget1.setGeometry(QtCore.QRect(450, 50, 131, 291))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Vx = QtWidgets.QLineEdit(self.widget1)
        self.Vx.setText('10')
        #self.Vx.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_2.addWidget(self.Vx)
        self.Vy = QtWidgets.QLineEdit(self.widget1)
        self.Vy.setText('0')
        self.verticalLayout_2.addWidget(self.Vy)
        self.time = QtWidgets.QLineEdit(self.widget1)
        self.time.setText('0.1')
        self.verticalLayout_2.addWidget(self.time)
        self.noise = QtWidgets.QLineEdit(self.widget1)
        self.noise.setText('100')
        self.verticalLayout_2.addWidget(self.noise)
        self.shift = QtWidgets.QLineEdit(self.widget1)
        self.shift.setText('0.1')
        self.verticalLayout_2.addWidget(self.shift)
        self.count = QtWidgets.QPushButton(self.tab)
        self.count.setGeometry(QtCore.QRect(270, 370, 161, 41))


        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.images = QtWidgets.QPushButton(self.tab_2)
        self.images.setGeometry(QtCore.QRect(170, 20, 361, 41))

        self.subframe = QtWidgets.QLabel(self.tab_2)
        self.subframe.setGeometry(QtCore.QRect(30, 100, 300, 300))
        self.readyframe = QtWidgets.QLabel(self.tab_2)
        self.readyframe.setGeometry(QtCore.QRect(360, 100, 300, 300))

        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(130, 410, 81, 21))
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(470, 410, 81, 21))
        self.tabWidget.addTab(self.tab_2, "")


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 547, 26))
        self.menubar.setNativeMenuBar(True)
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Имитатор"))
        self.Vx_label.setText(_translate("MainWindow", "Скорость по горизонтали, пикс/кадр:"))
        self.Vy_label.setText(_translate("MainWindow", "Скорость по вертикали, пикс/кадр:"))
        self.time_label.setText(_translate("MainWindow", "Время экспозиции, мс:"))
        self.noise_label.setText(_translate("MainWindow", "Шум, эл/выб:"))
        self.shift_label.setText(_translate("MainWindow", "Максимальное смещение субкадра, пикс:"))
        self.count.setText(_translate("MainWindow", "Рассчитать"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Расчет параметров"))
        self.images.setText(_translate("MainWindow", "Выбрать файлы..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Имитация смаза"))



class MyWin(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()  #экземпляр класса Ui_MainWindow, в нем конструктор всего GUI.
        self.ui.setupUi(self)      #инициализация GUI
        self.dialogCountParameters = Dialog(self)
        self.dialogSelectFiles = QtWidgets.QFileDialog()

        self.ui.count.clicked.connect(self.pushCount)
        self.ui.images.clicked.connect(self.selectFiles)



    def pushCount(self): #расчет параметров по нажатию кнопки

        frames, dtime, dnoise, dVx, dVy = self.countEvent()

        self.dialogCountParameters.frames.setText(str(frames))
        self.dialogCountParameters.dtime.setText(str(dtime))
        self.dialogCountParameters.dnoise.setText(str(dnoise))
        self.dialogCountParameters.dVx.setText(str(dVx))
        self.dialogCountParameters.dVy.setText(str(dVy))

        self.dialogCountParameters.exec()

    def countEvent(self):
        Vx = float(self.ui.Vx.text())
        Vy = float(self.ui.Vy.text())
        time = float(self.ui.time.text())
        noise = float(self.ui.noise.text())
        shift = float(self.ui.shift.text())

        frames = int(max(Vx, Vy) * time / shift)
        dtime = round(time / frames, 3)
        dnoise = round(noise / frames, 0)
        dVx = round(Vx / frames, 2)
        dVy = round(Vy / frames,2)

        return frames, dtime, dnoise, dVx, dVy

    def selectFiles(self):

        self.dialogSelectFiles.setFileMode(QtWidgets.QFileDialog.ExistingFiles) #открываю диалоговое окно для выбора файлов
        self.dialogSelectFiles.exec_()

        data = self.dialogSelectFiles.selectedFiles()

        self.getReadyFrame(data) #получаю смазанный кадр


        self.ui.label.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Субкадр</span></p></body></html>")
        self.ui.label_2.setText("<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Смаз</span></p></body></html>")

        subframe = Image.fromarray(self.ADC(np.loadtxt(data[0], skiprows=1))) #берем первый субкадр как образец
        subframe.save('subframe.jpeg')

        pixmap_subframe = QtGui.QPixmap('subframe.jpeg')
        pixmap_readyframe = QtGui.QPixmap('readyframe.jpeg')

        self.ui.subframe.setPixmap(pixmap_subframe.scaled(300, 300))
        self.ui.readyframe.setPixmap(pixmap_readyframe.scaled(300, 300))
        # self.ui.readyframe.setAlignment(QtGui.AlignCenter)



    def ADC(self, analog_arr, resolution=8):  #АЦП преобразование
        num_levels = 2 ** resolution
        level = np.max(analog_arr) / num_levels
        digital_arr = analog_arr / level
        digital_arr[digital_arr == 256] = 255 #level*num_levels = 256, значит для максимального значения будет 256, а надо 255

        return digital_arr.astype(np.uint8)

    def getReadyFrame(self, data): #получение смазанного кадра
        num_frames = int(self.dialogCountParameters.frames.toPlainText())
        vert_pixels = int(np.loadtxt(data[0], usecols=0, max_rows=1, ndmin=1)[0])
        hor_pixels = int(np.loadtxt(data[0], usecols=1, max_rows=1, ndmin=1)[0])

        file_array = np.zeros((num_frames, vert_pixels, hor_pixels))

        for i in range(num_frames):
            file_name = data[i]
            file_array[i] = np.loadtxt(file_name, skiprows=1)

        ready_array = np.zeros((vert_pixels, hor_pixels))
        for i in range(num_frames):
            ready_array += file_array[i]
        ready_array = self.ADC(ready_array)

        img = Image.fromarray(ready_array)
        img.save('readyframe.jpeg')




if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWin()
    window.show()
    sys.exit(app.exec_())
