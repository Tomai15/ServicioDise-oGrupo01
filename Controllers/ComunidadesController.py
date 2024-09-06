from DTOs.ComunidadesCercanasDTO import ComunidadesCercanasDTO
from Model.Ong import Ong
from Model.Persistente import Persistente
from Model.Ubicacion import Ubicacion
from Services.EncontrarComunidadesCercanas import EncontrarComunidadesCercanas


class ComunidadesController:
    def __init__(self, comunidadesService):
        self.comunidadesService = comunidadesService

    def comunidadesCercanasA (self, direccionDTO):

        encontrarComunidadesCercanasService = EncontrarComunidadesCercanas()
        listaComuninades = Ong.get_all()

        comunidadesARetornar= encontrarComunidadesCercanasService.encontrarComunidadesCercanas(direccionDTO,listaComuninades)

        comunidadesADTO=[]
        for comunidad in comunidadesARetornar:
            comunidadesADTO.append((comunidad.nombre, comunidad.direccion))
        comunidadDto= ComunidadesCercanasDTO(comunidadesADTO)
        return comunidadDto

    def crearComunidad(self,nuevaComunidadDTO):
        ubicacion = Ubicacion(nuevaComunidadDTO.latitud, nuevaComunidadDTO.longitud)
        nuevaComunidad = Ong(nuevaComunidadDTO.nombre,nuevaComunidadDTO.direccion,ubicacion)
        nuevaComunidad.save()