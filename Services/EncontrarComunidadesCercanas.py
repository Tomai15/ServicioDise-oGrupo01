from geopy import Nominatim
from geopy.distance import geodesic

from Model import Ong
from Model.Ubicacion import Ubicacion


class EncontrarComunidadesCercanas:
    def __init__(self):
        pass

    def encontrarComunidadesCercanas(self, direccionDTO,listaComunidades):

        geolocator = Nominatim(user_agent="geoapiExercises")

        cordenadasUsuario = geolocator.geocode(direccionDTO.direccion)

        if cordenadasUsuario is None:
            raise ValueError("Dirección no encontrada.")

        ubicacion_usuario = Ubicacion(cordenadasUsuario.latitude, cordenadasUsuario.longitude)

        # Calcular la distancia a cada ONG
        """
        distancias = []
        for ong in self.ongs:
            distancia = geodesic((ubicacion_usuario.latitud, ubicacion_usuario.longitud),
                                 (ong.ubicacion.latitud, ong.ubicacion.longitud)).kilometers
            distancias.append((ong, distancia))
    """
        # Ordenar las ONGs por distancia
        listaComunidades.sort(
                                key=lambda ong:
                                geodesic((ubicacion_usuario.latitud, ubicacion_usuario.longitud),
                                         (ong.ubicacion.latitud, ong.ubicacion.longitud)).
                                kilometers

                              )

        # Seleccionar las N ONGs más cercanas
        recomendadas = listaComunidades[:direccionDTO.getCantidad_recomendaciones()]
        return recomendadas
