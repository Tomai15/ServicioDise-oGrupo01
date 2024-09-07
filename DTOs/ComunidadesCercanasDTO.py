#Devuelve las comunidadesCercanas

class ComunidadesCercanasDTO:
    def __init__(self, comunidades):
        self.comunidades = comunidades
        #comunidades es una lista de duplas: (nombre, direccion)

    def to_dict(self):
        return {"comunidades": self.comunidades}