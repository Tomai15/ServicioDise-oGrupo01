#Envia los datos para encontrar las comunidades cercanas

class DireccionDTO:
    def __init__(self, direccion, cantidad_recomendaciones):
        self.direccion = direccion
        self.cantidad_recomendaciones = cantidad_recomendaciones

    def get_direccion(self):
        return self.direccion

    def getCantidad_recomendaciones(self):
        return self.cantidad_recomendaciones