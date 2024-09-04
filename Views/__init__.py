# views/item_view.py
from flask import Blueprint, request, jsonify

# Importamos el controlador o las funciones que necesitemos
from controllers.recomendadorDeUbicaciones_controller import generar_lista_ubicaciones # get_items, get_item

item_bp = Blueprint('item_bp', __name__)

# Recibe un string y un número n y devuelve una lista de strings de longitud n
@item_bp.route('/generate_list', methods=['POST'])
def generate_list_view():
    # Obtenemos el contenido JSON de la solicitud
    data = request.get_json()

    # Extraemos los parámetros del JSON
    direccion = data.get('direccion', '')
    cantidadDeComunidades = data.get('cantidadDeComunidades', 0)

    # Validamos los parámetros
    if not isinstance(direccion, str) or not isinstance(n, int) or n < 0:
        return jsonify({'error': 'Parámetros inválidos'}), 400

    # Llamar al controlador para obtener la lista de objetos
    lista_ubicaciones = generar_lista_ubicaciones(input_string, n)

    if lista_ubicaciones is None:
        return jsonify({'error': 'Error al generar la lista'}), 500
    else:
        lista_ubicaciones = ubicaciones.to_dict()
        # ubicaciones es el DTO que tiene la lista de ubicaciones de las comunidades
        return jsonify(lista_ubicaciones), 200
    """
    La vista llama al método generate_list del controlador, que devuelve una lista de objetos CustomItem 
    y un código de estado HTTP (status_code).
    """

    # Convertir cada objeto a un diccionario antes de devolver como JSON


