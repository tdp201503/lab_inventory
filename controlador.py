import time

from PyQt4 import QtGui, QtCore

from vista.lab_inventory import Ui_MainWindow as LabInventoryUI

from vista.agregar_o_modificar_item import Ui_Dialog as AgregarOModificarUI
from vista.informe_progreso import Ui_Dialog as InformeProgresoUI
from vista.acerca import Ui_Dialog as AcercaUI
from vista.buscar_items import Ui_Dialog as BuscarItemsUI
from vista.devolver_item import Ui_Dialog as DevolverItemUI
from vista.eliminar_item import Ui_Dialog as EliminarItemUI
from vista.prestar_item import Ui_Dialog as PrestarItemUI
from vista.reportes import Ui_Dialog as ReportesUI

from modelo.item import Item
from modelo.prestamo import Prestamo

import mysql.connector

from persistencia.base_datos import BaseDatos

# Informacion para conexion a base de datos
URL = 'localhost'
USUARIO = 'root'
CONTRASENA = '12345' #change password
NOMBRE_BD   = 'lab_inventory'

# Enumeracion para los tipos de mensajes
(ERROR, INFO, ADVER) = (1, 2, 3)

# Enumeracion para los tipos de operacion en base de datos (CRUD)
(INSERT, UPDATE, DELETE) = (10, 20, 30)


class LabInventoryController(QtGui.QMainWindow, LabInventoryUI):

	def __init__(self):
		super(self.__class__, self).__init__()
		self.setupUi(self)
		
		# Inicializacion de base de datos
		self.bd = BaseDatos(URL, USUARIO, CONTRASENA, NOMBRE_BD)
		
		# Banderas para inicializacion de tablas
		self.tabla_items_inicializada = False
		self.tabla_prestamos_inicializada = False
		
		# Variables para manejo de barra de progreso
		self.sleep_barra = 0.0
		self.step_barra = 0.0
		
		# Variable que almacena el Id del Item actualmente seleccionado
		self.current_item_id = 0
		self.current_prestamo_id = 0
		
		# Inicializacion de dialogos
		
		# Dialogo Informe Progreso
		self.dialogo_informe_progreso = QtGui.QDialog(self)
		self.ui_dialogo_informe_progreso = InformeProgresoUI()
		self.ui_dialogo_informe_progreso.setupUi(self.dialogo_informe_progreso)
		
		# Dialogo Agregar o Modificar Item
		self.dialogo_agregar_o_modificar_item = QtGui.QDialog(self)
		self.ui_dialogo_agregar_o_modificar_item = AgregarOModificarUI()
		self.ui_dialogo_agregar_o_modificar_item.setupUi(self.dialogo_agregar_o_modificar_item)
		
		# Dialogo Acerca del Programa
		self.dialogo_acerca = QtGui.QDialog(self)
		self.ui_dialogo_acerca = AcercaUI()
		self.ui_dialogo_acerca.setupUi(self.dialogo_acerca)
		
		# Dialogo Eliminar Item
		self.dialogo_eliminar_item = QtGui.QDialog(self)
		self.ui_dialogo_eliminar_item = EliminarItemUI()
		self.ui_dialogo_eliminar_item.setupUi(self.dialogo_eliminar_item)
		
		# Dialogo Buscar Items
		self.dialogo_buscar_items = QtGui.QDialog(self)
		self.ui_dialogo_buscar_items = BuscarItemsUI()
		self.ui_dialogo_buscar_items.setupUi(self.dialogo_buscar_items)
		
		# Dialogo Prestar Item
		self.dialogo_prestar_item = QtGui.QDialog(self)
		self.ui_dialogo_prestar_item = PrestarItemUI()
		self.ui_dialogo_prestar_item.setupUi(self.dialogo_prestar_item)
		
		# Dialogo Devolver Item
		self.dialogo_devolver_item = QtGui.QDialog(self)
		self.ui_dialogo_devolver_item = DevolverItemUI()
		self.ui_dialogo_devolver_item.setupUi(self.dialogo_devolver_item)
		
		# Dialogo Reportes
		self.dialogo_reportes = QtGui.QDialog(self)
		self.ui_dialogo_reportes = ReportesUI()
		self.ui_dialogo_reportes.setupUi(self.dialogo_reportes)
		
		# Conexion de senales para botones.
		
		# Listar Items
		self.boton_listar_items.clicked.connect(self.listar_items)
		
		# Mostrar Agregar Item
		self.boton_agregar_item.clicked.connect(self.mostrar_agregar_item)
		
		# Mostrar Modificar Item
		self.boton_modificar_item.clicked.connect(self.mostrar_modificar_item)
		
		# Mostrar Acerca de Programa
		self.boton_acerca.clicked.connect(self.mostrar_acerca)
		
		# Mostrar Eliminar Item
		self.boton_eliminar_item.clicked.connect(self.mostrar_eliminar_item)
		
		# Aceptar Eliminar Item
		self.ui_dialogo_eliminar_item.botones_eliminar_item.accepted.connect(self.eliminar_item)
		
		# Mostrar Buscar Items
		self.boton_buscar_items.clicked.connect(self.mostrar_buscar_items)
		
		# Mostrar Prestar Item
		self.boton_prestar_item.clicked.connect(self.mostrar_prestar_item)
		
		# Mostrar Devolver Item
		self.boton_devolver_item.clicked.connect(self.mostrar_devolver_item)
		
		# Mostrar Reportes
		self.boton_reportes.clicked.connect(self.mostrar_reportes)
		
		# Actualizar botones segun seleccion de tabla items
		self.tabla_items.selectionModel().selectionChanged.connect(self.item_seleccionado)
		
		# Actualizar botones segun seleccion de tabla prestamos
		self.tabla_prestamos.selectionModel().selectionChanged.connect(self.prestamo_seleccionado)
		
	def mostrar_mensaje(self, mensaje, tipo = INFO):
		titulo = self.windowTitle()
		if tipo == ADVER: # Mostrar mensaje de advertencia
			QtGui.QMessageBox.warning(self, titulo, mensaje) 
		elif tipo == ERROR: # Mostrar mensaje de error
			QtGui.QMessageBox.critical(self, titulo, mensaje)
		else: # Mostrar mensaje de informacion
			QtGui.QMessageBox.information(self, titulo, mensaje)
		
	def leer_datos_bd(self, comando):
		try:
			self.bd.connect()
		except mysql.connector.OperationalError, ex_c:
			self.mostrar_mensaje(str(ex_c), ERROR)
			return None
		
		cursor = None
		try:
			cursor  = self.bd.execute(comando)
		except mysql.connector.ProgrammingError, ex_q:
			self.mostrar_mensaje(str(ex_q), ERROR)
			return None
		except mysql.connector.OperationalError, ex_w:
			self.mostrar_mensaje(str(ex_w), ADVER)
			return None
		
		self.bd.close()
		
		# get data 
		data = []
		while (True):
			row = cursor.fetchone()
			if row == None:
				break
			data.append(row)
		
		cursor.close()
		del cursor
		return data
	
	def ejecutar_operacion(self, op):
		
		commdb = "" 
		
		if op == INSERT:
			datos = [
				str(self.ui_dialogo_agregar_o_modificar_item.nombre_item.text()), 
				str(self.ui_dialogo_agregar_o_modificar_item.descripcion_item.toPlainText()), 
				str(self.ui_dialogo_agregar_o_modificar_item.numero_existencias.value()), 
				str(self.ui_dialogo_agregar_o_modificar_item.cantidades_prestadas.value()),
				str(self.ui_dialogo_agregar_o_modificar_item.valor_comercial.text()),
				str(self.ui_dialogo_agregar_o_modificar_item.fecha_adquisicion.dateTime().toString(self.ui_dialogo_agregar_o_modificar_item.fecha_adquisicion.displayFormat())), 
				str(self.ui_dialogo_agregar_o_modificar_item.fecha_ultimo_prestamo.dateTime().toString(self.ui_dialogo_agregar_o_modificar_item.fecha_ultimo_prestamo.displayFormat()))
				]
			
			commdb = "insert into item(nombre, descripcion, numero_existencias, cantidades_prestadas, valor_comercial, fecha_adquisicion, fecha_ultimo_prestamo)" + " values('"+datos[0]+"','" + datos[1] + "','" +datos[2] + "','" + datos[3] + "','" +datos[4] + "','" +datos[5] + "','" +datos[6] + "')"
		elif op == UPDATE:
			datos = [
				str(self.leDni.text()), 
				str(self.leNames.text()), 
				str(self.leSurname.text()), 
				str(self.leDate.text())
			]
			commdb = "update "+TABLE_NAME['person']+" set Per_Names='"+ddb[1]+"', Per_Surname='"+ddb[2]+"', Per_Date='"+ddb[3]+"' where Per_Dni='"+ddb[0]+"'"
		elif op == DELETE:
			commdb = "delete from "+TABLE_NAME['person']+" where Per_Dni='"+ddb[0]+"'"
		
		print 'sql: ' + commdb
		
		try:
			self.bd.connect()
		except mysql.connector.OperationalError, ex_c:
			self.mostrar_mensaje(str(ex_c), ERROR)
			print str(ex_c)
			return
		
		correct = True		
		
		try:
			self.bd.execute(commdb)
			self.bd.commit();
		except mysql.connector.ProgrammingError, ex_q:
			self.mostrar_mensaje(str(ex_q), ERROR)
			print str(ex_q)
			correct = False
		except mysql.connector.OperationalError, ex_w:
			self.mostrar_mensaje(str(ex_w), ADVER)
			print str(ex_w)
			self.bd.rollback();
			correct = False
		except mysql.connector.IntegrityError, ex_i:
			self.mostrar_mensaje(str(ex_i), ADVER)
			print str(ex_i)
			correct = False
			
		self.bd.close();
		
		if correct:
			self.mostrar_mensaje('Operacion Correcta!')
			self.listar_items()
			print 'Operacion Correcta!'
		
	def iniciar_barra_progreso(self, mensaje, n_steps, sleep_barra):
		self.sleep_barra = sleep_barra
		self.barra_progreso.setEnabled(True)
		self.mensaje_progreso.setText(mensaje)
		self.barra_progreso.reset()
		self.step_barra = float(100.0/n_steps)

	def finalizar_barra_progreso(self, mensaje):
		self.barra_progreso.setEnabled(False)
		self.mensaje_progreso.setText(mensaje)

	def avanzar_barra_progreso(self, valor):
		time.sleep(self.sleep_barra)
		self.barra_progreso.setValue(valor * self.step_barra)
		
	def inicializar_tabla_items(self):
		encabezados_tabla_items = QtCore.QStringList()
		encabezados_tabla_items << "Id Item" << "Nombre" << "Existencias" << "Prestadas" << "Valor Comercial" << "Fecha Adquisicion"

		self.tabla_items.setSelectionMode(QtGui.QTableView.SingleSelection)
		self.tabla_items.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
		self.tabla_items.setColumnCount(6)
		self.tabla_items.setColumnWidth(0, 50)
		self.tabla_items.setColumnWidth(1, 200)
		self.tabla_items.setColumnWidth(2, 120)
		self.tabla_items.setColumnWidth(3, 120)
		self.tabla_items.setColumnWidth(4, 150)
		self.tabla_items.setColumnWidth(5, 150)
		self.tabla_items.setHorizontalHeaderLabels(encabezados_tabla_items)
		self.tabla_items.verticalHeader().setVisible(False)
		
	def listar_items(self):
		if not self.tabla_items_inicializada:
			self.inicializar_tabla_items();
			self.tabla_items_inicializada = True
		
		comando = "select id, nombre, numero_existencias, cantidades_prestadas, valor_comercial, fecha_adquisicion from item"
		data = self.leer_datos_bd(comando) 
		if data == None:
			return
		elif data == []:
			self.mostrar_mensaje('No hay datos en la tabla items!')
			return
		
		# Procesamiento de filas y columnas
		num_rows = len(data)
		num_cols = len(data[0])
		
		self.tabla_items.clearContents()
		
		self.tabla_items.setRowCount(num_rows)
		self.tabla_items.setColumnCount(num_cols)
		
		# set data table
		for i in range(num_rows):
			for j in range(num_cols):
				item = QtGui.QTableWidgetItem()
				#item.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled )
				item.setText(str(data[i][j]))
				self.tabla_items.setItem(i, j, item)
		
		self.tabla_items.resizeColumnsToContents()
		self.tabla_items.horizontalHeader().setStretchLastSection(True)
		
		self.boton_modificar_item.setEnabled(False)
		self.boton_eliminar_item.setEnabled(False)
		self.boton_prestar_item.setEnabled(False)
		self.boton_devolver_item.setEnabled(False)
		
	def inicializar_tabla_prestamos(self):
		encabezados_tabla_prestamos = QtCore.QStringList()
		encabezados_tabla_prestamos << "Id Prestamo" << "Documento Usuario" << "Cantidad Prestada" << "Fecha Prestamo"

		self.tabla_prestamos.setSelectionMode(QtGui.QTableView.SingleSelection)
		self.tabla_prestamos.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
		self.tabla_prestamos.setColumnCount(4)
		self.tabla_prestamos.setColumnWidth(0, 50)
		self.tabla_prestamos.setColumnWidth(1, 200)
		self.tabla_prestamos.setColumnWidth(2, 120)
		self.tabla_prestamos.setColumnWidth(3, 150)
		self.tabla_prestamos.setHorizontalHeaderLabels(encabezados_tabla_prestamos)
		self.tabla_prestamos.verticalHeader().setVisible(False)
		
	def listar_prestamos(self):
		if not self.tabla_prestamos_inicializada:
			self.inicializar_tabla_prestamos();
			self.tabla_prestamos_inicializada = True
			
		comando = "select id, documento_usuario, cantidad_prestada, fecha_prestamo from prestamo where id_item = " + str(self.current_item_id) + " and estado = 0"
		data = self.leer_datos_bd(comando) 
		if data == None:
			return
		elif data == []:
			self.tabla_prestamos.clearContents()
			self.tabla_prestamos.clearSelection()
			self.tabla_prestamos.setRowCount(0)
			self.mostrar_mensaje('No hay datos en la tabla prestamos!')
			return
		
		# Procesamiento de filas y columnas
		num_rows = len(data)
		num_cols = len(data[0])
		
		self.tabla_prestamos.clearContents()
		
		self.tabla_prestamos.setRowCount(num_rows)
		self.tabla_prestamos.setColumnCount(num_cols)
		
		# set data table
		for i in range(num_rows):
			for j in range(num_cols):
				prestamo = QtGui.QTableWidgetItem()
				#prestamo.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled )
				prestamo.setText(str(data[i][j]))
				self.tabla_prestamos.setItem(i, j, prestamo)
		
		self.tabla_prestamos.resizeColumnsToContents()
		self.tabla_prestamos.horizontalHeader().setStretchLastSection(True)
	
	def item_seleccionado(self, selected, deselected):
		if len(selected.indexes()) == 0:
			return
		
		cur_index = selected.indexes()[0]
		cur_row = cur_index.row()
		self.current_item_id = int(self.tabla_items.item(cur_row, 0).text())
		self.boton_modificar_item.setEnabled(True)
		self.boton_eliminar_item.setEnabled(True)
		self.boton_prestar_item.setEnabled(True)
		self.boton_devolver_item.setEnabled(False)
		self.tabla_prestamos.clearSelection()
		
		self.listar_prestamos()
		
	def prestamo_seleccionado(self, selected, deselected):
		if len(selected.indexes()) == 0:
			return
		
		cur_index = selected.indexes()[0]
		cur_row = cur_index.row()
		self.current_prestamo_id = int(self.tabla_prestamos.item(cur_row, 0).text())
		self.boton_devolver_item.setEnabled(True)
		print "Prestamo " + str(cur_row) + " seleccionado..."
	
	def reset_conexiones_agregar_modificar_item(self):
		try: self.ui_dialogo_agregar_o_modificar_item.boton_validar_agregar.clicked.disconnect()
		except Exception: pass
		
		try: self.ui_dialogo_agregar_o_modificar_item.boton_cancelar_agregar.clicked.disconnect()
		except Exception: pass
	
	def mostrar_agregar_item(self):
		self.dialogo_informe_progreso.exec_()
		self.dialogo_agregar_o_modificar_item.setWindowTitle("Agregar Item")
		self.ui_dialogo_agregar_o_modificar_item.boton_validar_agregar.setText("Agregar Item")
		
		self.reset_conexiones_agregar_modificar_item()
		self.ui_dialogo_agregar_o_modificar_item.boton_validar_agregar.clicked.connect(self.validar_agregar_item)
		self.ui_dialogo_agregar_o_modificar_item.boton_cancelar_agregar.clicked.connect(self.cancelar_agregar_item)
		self.dialogo_agregar_o_modificar_item.exec_()
		
	def validar_agregar_item(self):
		if len(self.ui_dialogo_agregar_o_modificar_item.nombre_item.text()) == 0:
			QtGui.QMessageBox.question(self.dialogo_agregar_o_modificar_item, 'Error de Validacion!', "Ingrese por favor un nombre para el item!", QtGui.QMessageBox.Ok)
			return
		
		self.ejecutar_operacion(INSERT)
		self.dialogo_agregar_o_modificar_item.close()
		
	def cancelar_agregar_item(self):
		self.dialogo_agregar_o_modificar_item.close()
		self.dialogo_informe_progreso.close()
		
	def mostrar_modificar_item(self):
		self.dialogo_agregar_o_modificar_item.setWindowTitle("Modificar Item")
		self.ui_dialogo_agregar_o_modificar_item.boton_validar_agregar.setText("Modificar Item")
		
		self.reset_conexiones_agregar_modificar_item()
		self.ui_dialogo_agregar_o_modificar_item.boton_validar_agregar.clicked.connect(self.validar_modificar_item)
		self.ui_dialogo_agregar_o_modificar_item.boton_cancelar_agregar.clicked.connect(self.cancelar_modificar_item)
		self.dialogo_agregar_o_modificar_item.exec_()
	
	def validar_modificar_item(self):
		if len(self.ui_dialogo_agregar_o_modificar_item.nombre_item.text()) == 0:
			QtGui.QMessageBox.question(self.dialogo_agregar_o_modificar_item, 'Error de Validacion!', "Ingrese por favor un nombre para el item!", QtGui.QMessageBox.Ok)
			return
		
		self.dialogo_agregar_o_modificar_item.close()
	
	def cancelar_modificar_item(self):
		self.dialogo_agregar_o_modificar_item.close()
	
	def mostrar_acerca(self):
		self.dialogo_acerca.exec_()
	
	def mostrar_eliminar_item(self):
		self.dialogo_eliminar_item.exec_()
	
	def eliminar_item(self):
		print "Eliminando item..."
	
	def mostrar_buscar_items(self):
		self.dialogo_buscar_items.exec_()
	
	def mostrar_prestar_item(self):
		self.dialogo_prestar_item.exec_()
	
	def mostrar_devolver_item(self):
		self.dialogo_devolver_item.exec_()
	
	def mostrar_reportes(self):
		self.ui_dialogo_reportes.parametros_reporte.setVisible(False)
		self.dialogo_reportes.exec_()
		
	
	
