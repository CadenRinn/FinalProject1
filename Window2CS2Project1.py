from PyQt5 import QtCore, QtGui, QtWidgets
#from CS2Project1 import *





class Ui_SecondWindow(object):
    username = ''
    password = ''
    def setupUi(self, SecondWindow) -> None:
        """
        Method that creates the Second Window and Widgets
        :param SecondWindow: Second Window from Qt Designer
        :return: None
        """
        SecondWindow.setObjectName("SecondWindow")
        SecondWindow.resize(700, 700)
        SecondWindow.setMinimumSize(QtCore.QSize(700, 700))
        SecondWindow.setMaximumSize(QtCore.QSize(700, 700))
        SecondWindow.setStyleSheet("background-color: rgb(172, 215, 255);")
        self.centralwidget = QtWidgets.QWidget(SecondWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.accountbalance_label = QtWidgets.QLabel(self.centralwidget)
        self.accountbalance_label.setGeometry(QtCore.QRect(180, 60, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.accountbalance_label.setFont(font)
        self.accountbalance_label.setObjectName("centralwidget")
        self.balancenumber_label = QtWidgets.QLabel(self.centralwidget)
        self.balancenumber_label.setGeometry(QtCore.QRect(170, 130, 321, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.balancenumber_label.setFont(font)
        self.balancenumber_label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.balancenumber_label.setText('$')
        self.balancenumber_label.setAlignment(QtCore.Qt.AlignCenter)
        self.balancenumber_label.setObjectName("balancenumber_label")
        self.deposit_input = QtWidgets.QLineEdit(self.centralwidget)
        self.deposit_input.setGeometry(QtCore.QRect(90, 270, 171, 41))
        self.deposit_input.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.deposit_input.setObjectName("deposit_input")
        self.withdraw_input = QtWidgets.QLineEdit(self.centralwidget)
        self.withdraw_input.setGeometry(QtCore.QRect(400, 270, 171, 41))
        self.withdraw_input.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.withdraw_input.setObjectName("withdraw_input")
        self.deposit_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.deposit())
        self.deposit_button.setGeometry(QtCore.QRect(70, 350, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.deposit_button.setFont(font)
        self.deposit_button.setStyleSheet("background-color: rgb(99, 159, 255);")
        self.deposit_button.setObjectName("deposit_button")
        self.withdraw_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.withdraw())
        self.withdraw_button.setGeometry(QtCore.QRect(380, 350, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.withdraw_button.setFont(font)
        self.withdraw_button.setStyleSheet("background-color: rgb(99, 159, 255);")
        self.withdraw_button.setObjectName("withdraw_button")
        self.accounterror_label = QtWidgets.QLabel(self.centralwidget)
        self.accounterror_label.setGeometry(QtCore.QRect(120, 470, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.accounterror_label.setFont(font)
        self.accounterror_label.setText("")
        self.accounterror_label.setAlignment(QtCore.Qt.AlignCenter)
        self.accounterror_label.setObjectName("accounterror_label")
        SecondWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SecondWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 26))
        self.menubar.setObjectName("menubar")
        SecondWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SecondWindow)
        self.statusbar.setObjectName("statusbar")
        SecondWindow.setStatusBar(self.statusbar)

        self.retranslateUi(SecondWindow)
        QtCore.QMetaObject.connectSlotsByName(SecondWindow)

    def retranslateUi(self, SecondWindow) -> None:
        """
        Method that sets the text and titles of widgets
        :param SecondWindow: Second Window from Qt Designer
        :return: None
        """
        _translate = QtCore.QCoreApplication.translate
        SecondWindow.setWindowTitle(_translate("SecondWindow", "MainWindow"))
        self.accountbalance_label.setText(_translate("SecondWindow", "Account Balance"))
        self.deposit_button.setText(_translate("SecondWindow", "Deposit"))
        self.withdraw_button.setText(_translate("SecondWindow", "Withdraw"))


    def deposit(self) -> None:
        """
        Method to deposit money to the Account Balance
        :return: None; Does modify account balance in UserCredentials
        """
        num1 = self.balancenumber_label.text()
        num3 = num1[1:]
        num = float(num3)
        try:
            num2 = float(self.deposit_input.text())
            if num2 <= 0:
                self.accounterror_label.setText('No change- Value is less than or equal to 0.')
            else:
                # Takes balancenumber_label and updates it while updating text file
                num += num2
                self.balancenumber_label.setText(f'${num:.2f}')
                word = self.balancenumber_label.text()
                word2 = word[1:]
                with open('UserCredentials', 'r') as f:
                    text = f.read()
                    text = text.replace(self.password + ' ' + num3, self.password + ' ' + word2)
                with open('UserCredentials', 'w') as f:
                    f.write(text)

        except:
            self.accounterror_label.setText('Error- Invalid Entry.')



    def withdraw(self) -> None:
        """
        Method to withdraw money from the Account Balance
        :return: None; does modify Account Balance in UserCredentials
        """
        num1 = self.balancenumber_label.text()
        num3 = num1[1:]
        num = float(num3)
        try:
            num2 = float(self.withdraw_input.text())
            if num2 <= 0:
                self.accounterror_label.setText('No change- Value is less than or equal to 0.')
            elif num2 > num:
                self.accounterror_label.setText('Cannot withdraw more than current account balance.')
            else:
                # Takes balancenumber_label and updates it while updating the text file
                num -= num2
                self.balancenumber_label.setText(f'${num:.2f}')
                word = self.balancenumber_label.text()
                word2 = word[1:]
                with open('UserCredentials', 'r') as f:
                    text = f.read()
                    text = text.replace(self.password + ' ' + num3, self.password + ' ' + word2)
                with open('UserCredentials', 'w') as f:
                    f.write(text)
        except:
            self.accounterror_label.setText('Error- Invalid Entry.')




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SecondWindow = QtWidgets.QMainWindow()
    ui = Ui_SecondWindow()
    ui.setupUi(SecondWindow)
    SecondWindow.show()
    sys.exit(app.exec_())