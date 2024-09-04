from geopy.geocoders import Nominatim
from geopy.distance import geodesic


class Ubicacion:
    def __init__(self, latitud, longitud):
        self.latitud = latitud
        self.longitud = longitud


class ONG:
    def __init__(self, nombre, direccion, ubicacion):
        self.nombre = nombre
        self.direccion = direccion
        self.ubicacion = ubicacion


class Direccion:
    def __init__(self, direccion, cantidad_recomendaciones):
        self.direccion = direccion
        self.cantidad_recomendaciones = cantidad_recomendaciones


class RecomendadorDeUbicaciones:
    def __init__(self):
        self.geolocator = Nominatim(user_agent="recomendador_ubicaciones")
        # ONGs hardcodeadas
        self.ongs = [
            ONG("ONG 1", "Calle Falsa 123, Ciudad, País", Ubicacion(-34.6037, -58.3816)),
            ONG("ONG 2", "Avenida Siempre Viva 742, Ciudad, País", Ubicacion(-33.8688, 151.2093)),
            ONG("ONG 3", "Bulevar de los Mártires 500, Ciudad, País", Ubicacion(40.7128, -74.0060)),
        ]

    def encontrarComunidadesCercanas(self, direccion_dto):
        # Obtener coordenadas de la dirección proporcionada
        location = self.geolocator.geocode(direccion_dto.direccion)
        if location is None:
            raise ValueError("Dirección no encontrada.")

        ubicacion_usuario = Ubicacion(location.latitude, location.longitude)

        # Calcular la distancia a cada ONG
        distancias = []
        for ong in self.ongs:
            distancia = geodesic((ubicacion_usuario.latitud, ubicacion_usuario.longitud),
                                 (ong.ubicacion.latitud, ong.ubicacion.longitud)).kilometers
            distancias.append((ong, distancia))

        # Ordenar las ONGs por distancia
        distancias.sort(key=lambda x: x[1])

        # Seleccionar las N ONGs más cercanas
        recomendadas = [ong for ong, _ in distancias[:direccion_dto.cantidad_recomendaciones]]
        return recomendadas


# Ejemplo de uso
if __name__ == "__main__":
    recomendador = RecomendadorDeUbicaciones()
    direccion = Direccion("Plaza de la República, Buenos Aires, Argentina", 2)
    recomendadas = recomendador.encontrarComunidadesCercanas(direccion)

    for ong in recomendadas:
        print(f"ONG recomendada: {ong.nombre}, Dirección: {ong.direccion}")
