CREATE TABLE IF NOT EXISTS `item` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) NOT NULL DEFAULT '0',
  `descripcion` varchar(255) NOT NULL DEFAULT '0',
  `numero_existencias` int(11) NOT NULL DEFAULT '0',
  `cantidad_disponible` int(11) NOT NULL DEFAULT '0',
  `valor_comercial` int(11) NOT NULL DEFAULT '0',
  `fecha_adquisicion` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `ultima_fecha_prestamo` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

INSERT INTO `item` (`id`, `nombre`, `descripcion`, `numero_existencias`, `cantidad_disponible`, `valor_comercial`, `fecha_adquisicion`, `ultima_fecha_prestamo`) VALUES
	(1, 'Osciloscopio', 'Herramienta para visualizar señales.', 3, 3, 5000000, '2012-10-10 10:00:00', '0000-00-00 00:00:00'),
	(2, 'Multimetro', 'Herramienta para realizar mediciones eléctricas.', 10, 10, 350000, '2010-05-05 12:00:00', '0000-00-00 00:00:00'),
	(3, 'Escopómetro', 'Herramienta para visualización de señales portátil.', 2, 2, 2500000, '2011-07-07 08:00:00', '0000-00-00 00:00:00');

-- Dumping structure for table lab_inventory.prestamo
CREATE TABLE IF NOT EXISTS `prestamo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `id_item` int(11) NOT NULL DEFAULT '0',
  `estado` tinyint(4) NOT NULL DEFAULT '0',
  `documento_usuario` varchar(20) NOT NULL DEFAULT '0',
  `cantidad_prestada` int(11) NOT NULL DEFAULT '0',
  `fecha_prestamo` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `fecha_devolucion` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `observaciones_devolucion` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `FK_prestamo_item` (`id_item`),
  CONSTRAINT `FK_prestamo_item` FOREIGN KEY (`id_item`) REFERENCES `item` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
