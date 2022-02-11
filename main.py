import datetime
import json
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QGridLayout, QMessageBox

from HanziField import HanziField
# from pyside6_loader import PySide6Ui
#
# # Convert file
# PySide6Ui("main_gui.ui").toPy()
import main_gui


class App(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = main_gui.Ui_MainWindow()
        self.ui.setupUi(self)

        f = open('hanzi.json')
        hanzi = json.load(f)
        # when finished, close the file
        f.close()
        self.hsk1_list = {}
        self.hsk2_list = {}
        self.hsk3_list = {}
        self.hsk4_list = {}
        self.hsk5_list = {}
        self.hsk6_list = {}
        self.hsk7_list = {}
        self.hsk8_list = {}
        self.hsk9_list = {}
        for key, value in hanzi.items():
            if value['level'] == 1:
                self.hsk1_list[key] = {'learned': value['learned'], 'level': value['level']}
            if value['level'] == 2:
                self.hsk2_list[key] = {'learned': value['learned'], 'level': value['level']}
            if value['level'] == 3:
                self.hsk3_list[key] = {'learned': value['learned'], 'level': value['level']}
            if value['level'] == 4:
                self.hsk4_list[key] = {'learned': value['learned'], 'level': value['level']}
            if value['level'] == 5:
                self.hsk5_list[key] = {'learned': value['learned'], 'level': value['level']}
            if value['level'] == 6:
                self.hsk6_list[key] = {'learned': value['learned'], 'level': value['level']}
            if value['level'] == 7:
                self.hsk7_list[key] = {'learned': value['learned'], 'level': value['level']}
            if value['level'] == 8:
                self.hsk8_list[key] = {'learned': value['learned'], 'level': value['level']}
            if value['level'] == 9:
                self.hsk9_list[key] = {'learned': value['learned'], 'level': value['level']}

        layoutHSK1 = QHBoxLayout()
        hsk1_hanzifield = HanziField(self.hsk1_list)
        layoutHSK1.setSpacing(0)
        layoutHSK1.setContentsMargins(0, 0, 0, 0)
        layoutHSK1.addWidget(hsk1_hanzifield)
        self.ui.HSK1.setLayout(layoutHSK1)

        layoutHSK2 = QHBoxLayout()
        hsk2_hanzifield = HanziField(self.hsk2_list)
        layoutHSK2.setSpacing(0)
        layoutHSK2.setContentsMargins(0, 0, 0, 0)
        layoutHSK2.addWidget(hsk2_hanzifield)
        self.ui.HSK2.setLayout(layoutHSK2)

        layoutHSK3 = QHBoxLayout()
        hsk3_hanzifield = HanziField(self.hsk3_list)
        layoutHSK3.setSpacing(0)
        layoutHSK3.setContentsMargins(0, 0, 0, 0)
        layoutHSK3.addWidget(hsk3_hanzifield)
        self.ui.HSK3.setLayout(layoutHSK3)

        layoutHSK4 = QHBoxLayout()
        hsk4_hanzifield = HanziField(self.hsk4_list)
        layoutHSK4.setSpacing(0)
        layoutHSK4.setContentsMargins(0, 0, 0, 0)
        layoutHSK4.addWidget(hsk4_hanzifield)
        self.ui.HSK4.setLayout(layoutHSK4)

        layoutHSK5 = QHBoxLayout()
        hsk5_hanzifield = HanziField(self.hsk5_list)
        layoutHSK5.setSpacing(0)
        layoutHSK5.setContentsMargins(0, 0, 0, 0)
        layoutHSK5.addWidget(hsk5_hanzifield)
        self.ui.HSK5.setLayout(layoutHSK5)

        layoutHSK6 = QHBoxLayout()
        hsk6_hanzifield = HanziField(self.hsk6_list)
        layoutHSK6.setSpacing(0)
        layoutHSK6.setContentsMargins(0, 0, 0, 0)
        layoutHSK6.addWidget(hsk6_hanzifield)
        self.ui.HSK6.setLayout(layoutHSK6)

        layoutHSK7 = QHBoxLayout()
        hsk7_hanzifield = HanziField(self.hsk7_list)
        layoutHSK7.setSpacing(0)
        layoutHSK7.setContentsMargins(0, 0, 0, 0)
        layoutHSK7.addWidget(hsk7_hanzifield)
        self.ui.HSK7.setLayout(layoutHSK7)

        layoutHSK8 = QHBoxLayout()
        hsk8_hanzifield = HanziField(self.hsk8_list)
        layoutHSK8.setSpacing(0)
        layoutHSK8.setContentsMargins(0, 0, 0, 0)
        layoutHSK8.addWidget(hsk8_hanzifield)
        self.ui.HSK8.setLayout(layoutHSK8)

        layoutHSK9 = QHBoxLayout()
        hsk9_hanzifield = HanziField(self.hsk9_list)
        layoutHSK9.setSpacing(0)
        layoutHSK9.setContentsMargins(0, 0, 0, 0)
        layoutHSK9.addWidget(hsk9_hanzifield)
        self.ui.HSK9.setLayout(layoutHSK9)
        self.ui.Save.clicked.connect(self.saveClicked)
        self.ui.Print.clicked.connect(self.showDialog)
        self.ui.statusbar.show()

    def saveClicked(self):
        for widget in self.ui.HSK1.children():
            if isinstance(widget, HanziField):
                for btn in widget.children():
                    if not isinstance(btn, QGridLayout):
                        self.hsk1_list[btn.text()]['learned'] = btn.isChecked()
        for widget in self.ui.HSK2.children():
            if isinstance(widget, HanziField):
                for btn in widget.children():
                    if not isinstance(btn, QGridLayout):
                        self.hsk2_list[btn.text()]['learned'] = btn.isChecked()
        for widget in self.ui.HSK3.children():
            if isinstance(widget, HanziField):
                for btn in widget.children():
                    if not isinstance(btn, QGridLayout):
                        self.hsk3_list[btn.text()]['learned'] = btn.isChecked()
        for widget in self.ui.HSK4.children():
            if isinstance(widget, HanziField):
                for btn in widget.children():
                    if not isinstance(btn, QGridLayout):
                        self.hsk4_list[btn.text()]['learned'] = btn.isChecked()
        for widget in self.ui.HSK5.children():
            if isinstance(widget, HanziField):
                for btn in widget.children():
                    if not isinstance(btn, QGridLayout):
                        self.hsk5_list[btn.text()]['learned'] = btn.isChecked()
        for widget in self.ui.HSK6.children():
            if isinstance(widget, HanziField):
                for btn in widget.children():
                    if not isinstance(btn, QGridLayout):
                        self.hsk6_list[btn.text()]['learned'] = btn.isChecked()
        for widget in self.ui.HSK7.children():
            if isinstance(widget, HanziField):
                for btn in widget.children():
                    if not isinstance(btn, QGridLayout):
                        self.hsk7_list[btn.text()]['learned'] = btn.isChecked()
        for widget in self.ui.HSK8.children():
            if isinstance(widget, HanziField):
                for btn in widget.children():
                    if not isinstance(btn, QGridLayout):
                        self.hsk8_list[btn.text()]['learned'] = btn.isChecked()
        for widget in self.ui.HSK9.children():
            if isinstance(widget, HanziField):
                for btn in widget.children():
                    if not isinstance(btn, QGridLayout):
                        self.hsk9_list[btn.text()]['learned'] = btn.isChecked()

        hsk_complete = self.hsk1_list | self.hsk2_list | self.hsk3_list | self.hsk4_list | self.hsk5_list
        hsk_complete |= self.hsk6_list | self.hsk7_list | self.hsk8_list | self.hsk9_list
        with open('hanzi.json', 'w') as f:
            json.dump(hsk_complete, f)
        status_text = "Saved " + datetime.datetime.now().strftime("%m.%d.%Y, %H:%M:%S")
        self.ui.statusbar.showMessage(status_text)

    def printClicked(self):
        pass



    def showDialog(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("print not yet implemented ")
        msgBox.setWindowTitle("Information")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.buttonClicked.connect(self.printClicked)

        returnValue = msgBox.exec()

if __name__ == '__main__':
    app = QApplication([])
    window = App()
    window.show()
    sys.exit(app.exec())
