class ComunidadesController:
    def __init__(self, comunidadesService):
        self.comunidadesService = comunidadesService
        #TODO: logica traer bd active record

    def comunidadesCercanasA (self, busquedaComunidadDTO):
        comunidadesARetornar= self.comunidadesService(self, busquedaComunidadDTO)
        comunidadesADTO=[]
        for comunidad in comunidadesARetornar:
            comunidadesADTO.append((comunidad.getNombre(), comunidad.getDireccion()))
        comunidadDto= ComunidadesCercanasDTO(comunidadesADTO)
        return comunidadDto
