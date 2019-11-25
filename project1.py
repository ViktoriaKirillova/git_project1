# - *- кодировка: utf-8 -*-

# Реализация формы, сгенерированная из чтения ui file ' UI.ui'
#
# Создано: PyQt5 генератор пользовательского кода 5.13.0
#
# Внимание! Все изменения, внесенные в этот файл, будут потеряны!


из PyQt5 импортируйте QtCore, QtGui, QtWidgets


класс  Ui_MainWindow (объект):
    def  setupUi (self, MainWindow):
 Главное окно.setObjectName ("MainWindow ")
 Главное окно.изменить размер( 542, 600)
        - я сам .centralwidget = QtWidgets.QWidget (MainWindow)
        - я сам .сентралвиджет.setObjectName ("centralwidget ")
        - я сам .кнопка = QtWidgets.QPushButton (self .centralwidget)
        - я сам .кнопка.setGeometry(QtCore.QRect( 160, 480, 211, 71))
 шрифт = QtGui.QFont()
 шрифт.setPointSize(17)
        - я сам .кнопка.setFont (шрифт)
        - я сам .кнопка.setObjectName ("кнопка")
 Главное окно.setCentralWidget (self .centralwidget)
        - я сам .линейка инструментов = QtWidgets.QMenuBar (MainWindow)
        - я сам .строка меню.setGeometry(QtCore.QRect( 0, 0, 542, 21))
        - я сам .строка меню.setObjectName ("menubar ")
 Главное окно.setMenuBar (self .строка меню)
        - я сам .строка состояния = QtWidgets.QStatusBar (MainWindow)
        - я сам .строка состояния.setObjectName ("строка состояния ")
 Главное окно.setStatusBar (self .строка состояния)

        - я сам .retranslateUi (MainWindow)
 QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def  retranslateUi (self, MainWindow):
 _translate = QtCore.QCoreApplication.переводить
 Главное окно.setWindowTitle (_translate ("MainWindow", " MainWindow "))
        - я сам .кнопка.setText(_translate("MainWindow", "Создать круг"))
