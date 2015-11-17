class Prestamo:
    def __init__(self, 
				id,
				id_item, 
				estado,
				documento_usuario, 
				cantidad_prestada, 
				fecha_prestamo,
				fecha_devolucion, 
				observaciones_devolucion):
		self.id = id
		self.id_item = id_item 
		self.estado = estado 
		self.documento_usuario = documento_usuario 
		self.cantidad_prestada = cantidad_prestada 
		self.fecha_prestamo = fecha_prestamo
		self.fecha_devolucion = fecha_devolucion 
		self.observaciones_devolucion = observaciones_devolucion
