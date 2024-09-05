def encontrarComunidadesCercanas(self, direccion_dto):
    ubicacion_usuario = Ubicacion(location.latitude, location.longitude)

    # Calcular la distancia a cada ONG
    """
    distancias = []
    for ong in self.ongs:
        distancia = geodesic((ubicacion_usuario.latitud, ubicacion_usuario.longitud),
                             (ong.ubicacion.latitud, ong.ubicacion.longitud)).kilometers
        distancias.append((ong, distancia))
"""
    # Ordenar las ONGs por distancia
    self.ongs.sort(key=lambda ong: geodesic((ubicacion_usuario.latitud, ubicacion_usuario.longitud),(ong.ubicacion.latitud, ong.ubicacion.longitud)).kilometers)

    # Seleccionar las N ONGs más cercanas
    recomendadas = self.ongs[:direccion_dto.cantidad_recomendaciones]
    return recomendadas
    # Obtener coordenadas de la dirección proporcionada
    location = self.geolocator.geocode(direccion_dto.direccion)
    if location is None:
        raise ValueError("Dirección no encontrada.")