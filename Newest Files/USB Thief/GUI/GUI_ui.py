# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUI.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpinBox, QWidget)
class Operation(object):
    def dr(self):
        print("hello")

op = Operation()
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(858, 627)
        Dialog.setMinimumSize(QSize(858, 627))
        Dialog.setMaximumSize(QSize(858, 627))
        Dialog.setWindowOpacity(2.000000000000000)
        Dialog.setAutoFillBackground(False)
        Dialog.setSizeGripEnabled(False)
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 100, 811, 141))
        self.widget.setStyleSheet(u"QWidget#widget\n"
"{\n"
"border:1px solid rgb(217, 217, 217)\n"
"}")
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 20, 61, 21))
        self.lineEdit_3 = QLineEdit(self.widget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(80, 20, 251, 23))
        self.pushButton_6 = QPushButton(self.widget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(340, 20, 80, 24))
        self.pushButton_6.clicked["bool"].connect(op.dr)
        self.label_14 = QLabel(self.widget)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(20, 70, 54, 16))
        self.lineEdit_6 = QLineEdit(self.widget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setEnabled(False)
        self.lineEdit_6.setGeometry(QRect(80, 70, 341, 23))
        self.label_15 = QLabel(self.widget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(20, 110, 411, 16))
        font = QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_19 = QLabel(self.widget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(460, 20, 54, 21))
        self.comboBox = QComboBox(self.widget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(520, 20, 271, 24))
        self.checkBox_9 = QCheckBox(self.widget)
        self.checkBox_9.setObjectName(u"checkBox_9")
        self.checkBox_9.setGeometry(QRect(460, 60, 121, 22))
        self.checkBox_10 = QCheckBox(self.widget)
        self.checkBox_10.setObjectName(u"checkBox_10")
        self.checkBox_10.setGeometry(QRect(460, 100, 121, 22))
        self.checkBox_11 = QCheckBox(self.widget)
        self.checkBox_11.setObjectName(u"checkBox_11")
        self.checkBox_11.setGeometry(QRect(620, 60, 161, 22))
        self.checkBox_12 = QCheckBox(self.widget)
        self.checkBox_12.setObjectName(u"checkBox_12")
        self.checkBox_12.setGeometry(QRect(620, 100, 121, 22))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 10, 61, 21))
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(100, 10, 621, 23))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 40, 781, 20))
        font1 = QFont()
        font1.setPointSize(13)
        self.label_2.setFont(font1)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(740, 10, 80, 24))
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(640, 490, 181, 31))
        font2 = QFont()
        font2.setPointSize(11)
        self.pushButton_2.setFont(font2)
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(40, 90, 51, 20))
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(Qt.LeftToRight)
        self.label_4.setAutoFillBackground(True)
        self.widget_2 = QWidget(Dialog)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(20, 280, 811, 141))
        self.widget_2.setStyleSheet(u"QWidget#widget_2\n"
"{\n"
"border:1px solid rgb(217, 217, 217)\n"
"}")
        self.label_9 = QLabel(self.widget_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 20, 231, 21))
        self.label_10 = QLabel(self.widget_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(310, 20, 111, 21))
        self.label_11 = QLabel(self.widget_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(20, 56, 54, 20))
        self.label_12 = QLabel(self.widget_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(80, 56, 91, 21))
        self.label_13 = QLabel(self.widget_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(220, 56, 54, 21))
        self.checkBox_3 = QCheckBox(self.widget_2)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setGeometry(QRect(290, 56, 111, 21))
        self.label_17 = QLabel(self.widget_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(430, 20, 71, 20))
        self.label_18 = QLabel(self.widget_2)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(430, 56, 71, 20))
        self.lineEdit_7 = QLineEdit(self.widget_2)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setGeometry(QRect(510, 20, 271, 23))
        self.lineEdit_8 = QLineEdit(self.widget_2)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setGeometry(QRect(510, 56, 271, 23))
        self.checkBox_4 = QCheckBox(self.widget_2)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setGeometry(QRect(20, 90, 81, 31))
        self.checkBox_5 = QCheckBox(self.widget_2)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setGeometry(QRect(140, 90, 81, 31))
        self.checkBox_6 = QCheckBox(self.widget_2)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setGeometry(QRect(260, 90, 121, 31))
        self.checkBox_7 = QCheckBox(self.widget_2)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setGeometry(QRect(420, 90, 191, 31))
        self.checkBox_8 = QCheckBox(self.widget_2)
        self.checkBox_8.setObjectName(u"checkBox_8")
        self.checkBox_8.setGeometry(QRect(650, 90, 131, 31))
        self.spinBox = QSpinBox(self.widget_2)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(170, 56, 42, 21))
        self.spinBox_2 = QSpinBox(self.widget_2)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setGeometry(QRect(250, 20, 61, 21))
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 270, 51, 21))
        self.label_5.setFont(font)
        self.label_5.setAutoFillBackground(True)
        self.widget_3 = QWidget(Dialog)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(20, 460, 441, 141))
        self.widget_3.setStyleSheet(u"QWidget#widget_3\n"
"{ \n"
"border:1px solid rgb(217, 217, 217)\n"
"}\n"
"")
        self.checkBox = QCheckBox(self.widget_3)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(30, 20, 121, 41))
        self.checkBox.setAutoFillBackground(False)
        self.checkBox_2 = QCheckBox(self.widget_3)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(30, 80, 121, 41))
        self.checkBox_2.setTabletTracking(False)
        self.checkBox_2.setAcceptDrops(False)
        self.checkBox_2.setStyleSheet(u"")
        self.lineEdit_2 = QLineEdit(self.widget_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(250, 30, 161, 21))
        self.label_3 = QLabel(self.widget_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(210, 30, 41, 21))
        self.label_3.setAutoFillBackground(False)
        self.pushButton_5 = QPushButton(self.widget_3)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(210, 91, 201, 20))
        self.checkBox_2.raise_()
        self.checkBox.raise_()
        self.lineEdit_2.raise_()
        self.label_3.raise_()
        self.pushButton_5.raise_()
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 450, 54, 21))
        self.label_6.setFont(font)
        self.label_6.setAutoFillBackground(True)
        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(640, 580, 181, 31))
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_7.setOpenExternalLinks(True)
        self.widget_4 = QWidget(Dialog)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(490, 459, 120, 141))
        self.widget_4.setStyleSheet(u"QWidget#widget_4\n"
"{ \n"
"border:1px solid rgb(217, 217, 217)\n"
"}\n"
"")
        self.pushButton_7 = QPushButton(self.widget_4)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(20, 20, 80, 24))
        self.pushButton_8 = QPushButton(self.widget_4)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(20, 60, 80, 24))
        self.pushButton_9 = QPushButton(self.widget_4)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(20, 100, 80, 24))
        self.label_16 = QLabel(Dialog)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(500, 450, 54, 16))
        self.label_16.setFont(font)
        self.label_16.setAutoFillBackground(True)
        self.label_20 = QLabel(Dialog)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(650, 555, 161, 21))
        self.label_20.setFont(font1)
        self.label_20.setAlignment(Qt.AlignCenter)
        self.label_20.setOpenExternalLinks(True)

        self.retranslateUi(Dialog)
        self.checkBox_9.clicked["bool"].connect(self.checkBox_10.setDisabled)
        self.checkBox_9.clicked["bool"].connect(self.checkBox_12.setDisabled)
        self.checkBox_9.clicked["bool"].connect(self.comboBox.setDisabled)
        self.checkBox_9.clicked["bool"].connect(self.lineEdit_6.setEnabled)
        self.checkBox_10.clicked["bool"].connect(self.checkBox_12.setDisabled)
        self.checkBox_10.clicked["bool"].connect(self.comboBox.setDisabled)
        self.checkBox_10.clicked["bool"].connect(self.checkBox_9.setDisabled)
        self.checkBox_10.clicked["bool"].connect(self.lineEdit_7.setDisabled)
        self.checkBox_10.clicked["bool"].connect(self.lineEdit_8.setDisabled)
        self.checkBox_9.clicked["bool"].connect(self.lineEdit_7.setDisabled)
        self.checkBox_9.clicked["bool"].connect(self.lineEdit_8.setDisabled)
        self.checkBox_3.clicked["bool"].connect(self.spinBox.setDisabled)

        self.pushButton_7.setDefault(False)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"USB_Thief\u914d\u7f6e\u6587\u4ef6\u7ba1\u7406\u5668V1.0", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"\u76ee\u6807\u76ee\u5f55\uff1a", None))
        self.pushButton_6.setText(QCoreApplication.translate("Dialog", u"\u6d4f\u89c8", None))
        self.label_14.setText(QCoreApplication.translate("Dialog", u"\u6587\u4ef6\u641c\u7d22\uff1a", None))
        self.label_15.setText(QCoreApplication.translate("Dialog", u"\u5982\u82e5\u641c\u7d22\u591a\u4e2a\u6587\u4ef6\u540d\u79f0\uff0c\u6587\u4ef6\u540d\u79f0\u95f4\u8bf7\u7528\u9017\u53f7\u95f4\u9694\u5f00\u3002\u8bf7\u4f7f\u7528\u82f1\u6587\u9017\u53f7", None))
        self.label_19.setText(QCoreApplication.translate("Dialog", u"\u6267\u884c\u64cd\u4f5c\uff1a", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"\u590d\u5236\u5f53\u524d\u76ee\u5f55\u4e0b\u5168\u90e8\u6587\u4ef6", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"\u590d\u5236\u5f53\u524d\u76ee\u5f55\u7684\u7279\u5b9a\u540e\u7f00\u6587\u4ef6", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"\u590d\u5236\u76ee\u5f55\u53ca\u5b50\u76ee\u5f55\u7684\u7279\u5b9a\u540e\u7f00\u6587\u4ef6", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Dialog", u"\u590d\u5236\u76ee\u5f55\u53ca\u5b50\u76ee\u5f55\u7684\u6587\u4ef6", None))

        self.checkBox_9.setText(QCoreApplication.translate("Dialog", u"\u542f\u7528\u6587\u4ef6\u641c\u7d22\u529f\u80fd", None))
        self.checkBox_10.setText(QCoreApplication.translate("Dialog", u"\u62f7\u8d1d\u6574\u4e2a\u6587\u4ef6\u5939", None))
        self.checkBox_11.setText(QCoreApplication.translate("Dialog", u"\u591a\u7ebf\u7a0b\u6267\u884c\u547d\u4ee4\uff08\u6d4b\u8bd5\u4e2d\uff09", None))
        self.checkBox_12.setText(QCoreApplication.translate("Dialog", u"\u4e0d\u8981\u590d\u5236\u7a7a\u6587\u4ef6\u5939", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u50a8\u5b58\u76ee\u5f55\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u9ed8\u8ba4\u4e3a\u4fdd\u5b58\u5230USB_Thief.exe\u540c\u76ee\u5f55\u4e0b\u7684USBThiefData\u6587\u4ef6\u5939\u5185", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u6d4f\u89c8", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"\u4fdd\u5b58\u8bbe\u7f6e", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u590d\u5236\u9009\u9879", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"\u5ef6\u8fdf\u64cd\u4f5c\uff1a\u5f53\u8fd0\u884cUSB_Thief.exe\u540e\uff0c\u5ef6\u8fdf", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u" \u79d2\u8fdb\u884c\u590d\u5236\u6587\u4ef6", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"\u5927\u5c0f\u9650\u5236\uff1a", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"\u590d\u5236\u5927\u5c0f\u4e0d\u8d85\u8fc7", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u"GB\u7684\u6587\u4ef6", None))
        self.checkBox_3.setText(QCoreApplication.translate("Dialog", u"\u6587\u4ef6\u5927\u5c0f\u65e0\u9650\u5236", None))
        self.label_17.setText(QCoreApplication.translate("Dialog", u"\u540e\u7f00\u540d\u767d\u540d\u5355", None))
        self.label_18.setText(QCoreApplication.translate("Dialog", u"\u540e\u7f00\u540d\u9ed1\u540d\u5355", None))
        self.checkBox_4.setText(QCoreApplication.translate("Dialog", u"\u53bb\u540e\u7f00\u6df7\u6dc6", None))
        self.checkBox_5.setText(QCoreApplication.translate("Dialog", u"\u53bb\u591a\u540e\u7f00", None))
        self.checkBox_6.setText(QCoreApplication.translate("Dialog", u"\u590d\u5236\u540e\u5220\u9664\u6e90\u6587\u4ef6", None))
        self.checkBox_7.setText(QCoreApplication.translate("Dialog", u"\u590d\u5236\u65e0\u540e\u7f00\u6587\u4ef6(\u90e8\u5206\u529f\u80fd\u7981\u6b62)", None))
        self.checkBox_8.setText(QCoreApplication.translate("Dialog", u"\u6587\u4ef6\u91cd\u590d\u5219\u5220\u9664\u65e7\u7684", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u590d\u5236\u64cd\u4f5c", None))
        self.checkBox.setText(QCoreApplication.translate("Dialog", u"\u6587\u4ef6\u540d\u79f0\u52a0\u5bc6\u9690\u85cf", None))
        self.checkBox_2.setText(QCoreApplication.translate("Dialog", u"\u6587\u4ef6\u540e\u7f00\u52a0\u5bc6\u9690\u85cf", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u72b6\u6001\uff1a", None))
        self.pushButton_5.setText(QCoreApplication.translate("Dialog", u"\u89e3\u5bc6", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u9ad8\u7ea7\u9009\u9879", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><a href=\"https://github.com/ZeronesNet/USB_Thief\"><span style=\" text-decoration: underline; color:#0000ff;\">\u66f4\u65b0\u7248\u672c\u8bf7\u8bbf\u95ee\u4f5c\u8005\u4e2a\u4eba\u4e3b\u9875</span></a></p></body></html>", None))
        self.pushButton_7.setText(QCoreApplication.translate("Dialog", u"\u68c0\u6d4b\u811a\u672c\u529f\u80fd", None))
        self.pushButton_8.setText(QCoreApplication.translate("Dialog", u"\u67e5\u770b\u914d\u7f6e", None))
        self.pushButton_9.setText(QCoreApplication.translate("Dialog", u"\u67e5\u770b\u65e5\u5fd7", None))
        self.label_16.setText(QCoreApplication.translate("Dialog", u"\u5e2e\u52a9\u6307\u4ee4", None))
        self.label_20.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><a href=\"https://github.com/ZeronesNet/USB_Thief/blob/main/%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8E.txt\"><span style=\" text-decoration: underline; color:#0000ff;\">\u7a0b\u5e8f\u4f7f\u7528\u8bf4\u660e</span></a></p></body></html>", None))
    # retranslateUi

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QDialog()
    ui = Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())