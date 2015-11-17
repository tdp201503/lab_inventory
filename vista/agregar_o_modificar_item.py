# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'agregar_o_modificar_item.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.setWindowModality(QtCore.Qt.WindowModal)
        Dialog.resize(480, 417)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.nombre_item = QtGui.QLineEdit(Dialog)
        self.nombre_item.setObjectName(_fromUtf8("nombre_item"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.nombre_item)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.numero_existencias = QtGui.QSpinBox(Dialog)
        self.numero_existencias.setObjectName(_fromUtf8("numero_existencias"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.numero_existencias)
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_4)
        self.valor_comercial = QtGui.QLineEdit(Dialog)
        self.valor_comercial.setObjectName(_fromUtf8("valor_comercial"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.valor_comercial)
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_5)
        self.fecha_adquisicion = QtGui.QDateTimeEdit(Dialog)
        self.fecha_adquisicion.setDateTime(QtCore.QDateTime(QtCore.QDate(2015, 11, 16), QtCore.QTime(0, 0, 0)))
        self.fecha_adquisicion.setDate(QtCore.QDate(2015, 11, 16))
        self.fecha_adquisicion.setCalendarPopup(True)
        self.fecha_adquisicion.setObjectName(_fromUtf8("fecha_adquisicion"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.fecha_adquisicion)
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_6)
        self.fecha_ultimo_prestamo = QtGui.QDateTimeEdit(Dialog)
        self.fecha_ultimo_prestamo.setDateTime(QtCore.QDateTime(QtCore.QDate(2015, 11, 16), QtCore.QTime(0, 0, 0)))
        self.fecha_ultimo_prestamo.setCalendarPopup(True)
        self.fecha_ultimo_prestamo.setObjectName(_fromUtf8("fecha_ultimo_prestamo"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.fecha_ultimo_prestamo)
        self.descripcion_item = QtGui.QPlainTextEdit(Dialog)
        self.descripcion_item.setObjectName(_fromUtf8("descripcion_item"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.descripcion_item)
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_7)
        self.cantidades_prestadas = QtGui.QSpinBox(Dialog)
        self.cantidades_prestadas.setObjectName(_fromUtf8("cantidades_prestadas"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.cantidades_prestadas)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.boton_validar_agregar = QtGui.QPushButton(Dialog)
        self.boton_validar_agregar.setObjectName(_fromUtf8("boton_validar_agregar"))
        self.horizontalLayout.addWidget(self.boton_validar_agregar)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.boton_cancelar_agregar = QtGui.QPushButton(Dialog)
        self.boton_cancelar_agregar.setObjectName(_fromUtf8("boton_cancelar_agregar"))
        self.horizontalLayout.addWidget(self.boton_cancelar_agregar)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Agregar o Modificar Item", None))
        self.label.setText(_translate("Dialog", "Nombre", None))
        self.label_2.setText(_translate("Dialog", "Descripción", None))
        self.label_3.setText(_translate("Dialog", "Número de Existencias", None))
        self.label_4.setText(_translate("Dialog", "Valor Comercial", None))
        self.label_5.setText(_translate("Dialog", "Fecha Adquisición", None))
        self.fecha_adquisicion.setDisplayFormat(_translate("Dialog", "yyyy-MM-dd hh:mm:ss", None))
        self.label_6.setText(_translate("Dialog", "Fecha Último Préstamo", None))
        self.fecha_ultimo_prestamo.setDisplayFormat(_translate("Dialog", "yyyy-MM-dd hh:mm:ss", None))
        self.label_7.setText(_translate("Dialog", "Cantidades Prestadas", None))
        self.boton_validar_agregar.setText(_translate("Dialog", "Agregar Item", None))
        self.boton_cancelar_agregar.setText(_translate("Dialog", "Cancelar", None))

