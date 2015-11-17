# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lab_inventory.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1135, 563)
        MainWindow.setStyleSheet(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(":/imagenes/recursos/scientist.png")))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_3.addWidget(self.label)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.boton_acerca = QtGui.QPushButton(self.centralwidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/imagenes/recursos/information3.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.boton_acerca.setIcon(icon)
        self.boton_acerca.setObjectName(_fromUtf8("boton_acerca"))
        self.horizontalLayout_3.addWidget(self.boton_acerca)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem4 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.boton_listar_items = QtGui.QPushButton(self.centralwidget)
        self.boton_listar_items.setObjectName(_fromUtf8("boton_listar_items"))
        self.horizontalLayout_2.addWidget(self.boton_listar_items)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.boton_agregar_item = QtGui.QPushButton(self.centralwidget)
        self.boton_agregar_item.setObjectName(_fromUtf8("boton_agregar_item"))
        self.horizontalLayout_2.addWidget(self.boton_agregar_item)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.boton_modificar_item = QtGui.QPushButton(self.centralwidget)
        self.boton_modificar_item.setEnabled(False)
        self.boton_modificar_item.setObjectName(_fromUtf8("boton_modificar_item"))
        self.horizontalLayout_2.addWidget(self.boton_modificar_item)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.boton_eliminar_item = QtGui.QPushButton(self.centralwidget)
        self.boton_eliminar_item.setEnabled(False)
        self.boton_eliminar_item.setObjectName(_fromUtf8("boton_eliminar_item"))
        self.horizontalLayout_2.addWidget(self.boton_eliminar_item)
        spacerItem8 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem8)
        self.boton_buscar_items = QtGui.QPushButton(self.centralwidget)
        self.boton_buscar_items.setObjectName(_fromUtf8("boton_buscar_items"))
        self.horizontalLayout_2.addWidget(self.boton_buscar_items)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tabla_items = QtGui.QTableWidget(self.centralwidget)
        self.tabla_items.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tabla_items.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tabla_items.setObjectName(_fromUtf8("tabla_items"))
        self.tabla_items.setColumnCount(0)
        self.tabla_items.setRowCount(0)
        self.verticalLayout.addWidget(self.tabla_items)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        spacerItem9 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem9)
        self.boton_prestar_item = QtGui.QPushButton(self.centralwidget)
        self.boton_prestar_item.setEnabled(False)
        self.boton_prestar_item.setObjectName(_fromUtf8("boton_prestar_item"))
        self.horizontalLayout_5.addWidget(self.boton_prestar_item)
        spacerItem10 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem10)
        self.boton_devolver_item = QtGui.QPushButton(self.centralwidget)
        self.boton_devolver_item.setEnabled(False)
        self.boton_devolver_item.setObjectName(_fromUtf8("boton_devolver_item"))
        self.horizontalLayout_5.addWidget(self.boton_devolver_item)
        spacerItem11 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem11)
        self.boton_reportes = QtGui.QPushButton(self.centralwidget)
        self.boton_reportes.setObjectName(_fromUtf8("boton_reportes"))
        self.horizontalLayout_5.addWidget(self.boton_reportes)
        spacerItem12 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem12)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.tabla_prestamos = QtGui.QTableWidget(self.centralwidget)
        self.tabla_prestamos.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tabla_prestamos.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tabla_prestamos.setObjectName(_fromUtf8("tabla_prestamos"))
        self.tabla_prestamos.setColumnCount(0)
        self.tabla_prestamos.setRowCount(0)
        self.verticalLayout.addWidget(self.tabla_prestamos)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "LabInventory", None))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#000000;\">Lab Inventory</span></p><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#000000;\">Versión 1.0.0</span></p><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#000000;\">Noviembre 16 de 2015</span></p></body></html>", None))
        self.boton_acerca.setText(_translate("MainWindow", "Acerca de este programa", None))
        self.boton_listar_items.setText(_translate("MainWindow", "Listar Items", None))
        self.boton_agregar_item.setText(_translate("MainWindow", "Agregar Item", None))
        self.boton_modificar_item.setText(_translate("MainWindow", "Modificar Item", None))
        self.boton_eliminar_item.setText(_translate("MainWindow", "Eliminar Item", None))
        self.boton_buscar_items.setText(_translate("MainWindow", "Buscar Items", None))
        self.boton_prestar_item.setText(_translate("MainWindow", "Prestar Item", None))
        self.boton_devolver_item.setText(_translate("MainWindow", "Devolver Item", None))
        self.boton_reportes.setText(_translate("MainWindow", "Reportes", None))

import recursos_rc
