import sys

from PySide6.QtCore import QSize
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QWidget, QPushButton, QApplication, QGridLayout


class HanziButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super(HanziButton, self).__init__(*args, **kwargs)
        self.setFont(QFont("KaiTi", 25))
        self.setFlat(True)
        self.setStyleSheet("QPushButton:checked { background-color: rgb(125, 166, 125);} QToolTip {border: 2px solid "
                           "darkkhaki;padding: 5px;border-radius: 3px;opacity: 200;font: bold 80px;font-family: "
                           "'KaiTi';}")
        self.setFixedSize(QSize(42, 42))
        self.setCheckable(True)

    def btnClicked(self, state):
        self.setChecked(state)

    def cheEvent(self, event):
        pass


class HanziField(QWidget):
    def __init__(self, hsklist, *args, **kwargs):
        super(HanziField, self).__init__(*args, **kwargs)
        layout = QGridLayout()
        layout.setSpacing(0)
        self.setLayout(layout)

        textHsk = list(hsklist.keys())

        length = len(textHsk)
        for i in range(1, length + 1):
            globals()[f"b_{i}"] = HanziButton()
            globals()[f"b_{i}"].clicked.connect(globals()[f"b_{i}"].btnClicked)
        h_range: int
        v_range, h_range = 0, 0
        for i in range(1, length + 1):
            globals()[f"b_{i}"].setText(textHsk[0])
            globals()[f"b_{i}"].setToolTip(textHsk[0])
            if hsklist[textHsk[0]]['learned']:
                globals()[f"b_{i}"].setChecked(True)
            textHsk.pop(0)
            layout.addWidget(globals()[f"b_{i}"], h_range, v_range)
            v_range += 1
            if v_range == 25:
                h_range += 1
                v_range = 0


def main():
    app = QApplication(sys.argv)
    test = {"\u6211": {"learned": True, "level": 1}, }
    hz = HanziField(test)
    hz.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
