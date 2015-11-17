class Item:
    def __init__(self, 
				id,
				nombre, 
				descripcion, 
				numero_existencias,
				cantidad_disponible,
				valor_comercial, 
				fecha_adquisicion,
				ultima_fecha_prestamo):
		self.id = id
		self.nombre = nombre 
		self.descripcion = descripcion 
		self.numero_existencias = numero_existencias
		self.cantidad_disponible = cantidad_disponible
		self.valor_comercial = valor_comercial 
		self.fecha_adquisicion = fecha_adquisicion
		self.ultima_fecha_prestamo = ultima_fecha_prestamo
