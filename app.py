from flask import Flask, Blueprint, request, jsonify
import Configuracion
from Controllers.ComunidadesController import ComunidadesController
from DTOs.DireccionDTO import DireccionDTO
from DTOs.NuevaComunidadDTO import NuevaComunidadDTO
from Model.Ubicacion import Ubicacion
from Services.EncontrarComunidadesCercanas import EncontrarComunidadesCercanas
from database import db

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+mysqldb://{Configuracion.MYSQL_USER}:{Configuracion.MYSQL_PASSWORD}@{Configuracion.MYSQL_HOST}:{Configuracion.MYSQL_PORT}/{Configuracion.MYSQL_DB}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)

def create_db():
    with app.app_context():
        db.create_all()
create_db()
item_bp = Blueprint('item_bp', __name__)

# Recibe un string y un número n y devuelve una lista de strings de longitud n
@item_bp.route('/generate_list', methods=['POST'])
def generate_list_view():

    controllerComunidades = ComunidadesController(EncontrarComunidadesCercanas())

    # Obtenemos el contenido JSON de la solicitud
    data = request.get_json()

    # Extraemos los parámetros del JSON
    direccion = data.get('direccion', '')
    cantidadDeComunidades = data.get('cantidadDeComunidades', 0)

    # Validamos los parámetros
    if not isinstance(direccion, str) or not isinstance(cantidadDeComunidades, int) or cantidadDeComunidades < 0:
        return jsonify({'error': 'Parámetros inválidos'}), 400

    direccionDTO = DireccionDTO(direccion,cantidadDeComunidades)
    # Llamar al controlador para obtener la lista de objetos
    comunidadesCercanasDTO = controllerComunidades.comunidadesCercanasA(direccionDTO)

    if comunidadesCercanasDTO is None:
        return jsonify({'error': 'Error al generar la lista'}), 500
    else:
        # ubicaciones es el DTO que tiene la lista de ubicaciones de las comunidades
        return jsonify({'Comunidades': comunidadesCercanasDTO}), 200

    """
    La vista llama al método generate_list del controlador, que devuelve una lista de objetos CustomItem 
    y un código de estado HTTP (status_code).
    """
@item_bp.route('/agregar_comunidad', methods=['POST'])
def agregar_comunidad():
    controllerComunidades = ComunidadesController(EncontrarComunidadesCercanas())

    # Obtenemos el contenido JSON de la solicitud
    data = request.get_json()

    # Extraemos los parámetros del JSON
    nombre = data.get('nombre', '')
    direccion = data.get('direccion', '')
    latitud = data.get("ubicacion").get("latitud")
    longitud = data.get("ubicacion").get("longitud")

    nuevaComunidadDTO = NuevaComunidadDTO(nombre,direccion, latitud, longitud)
    controllerComunidades.crearComunidad(nuevaComunidadDTO)

    return jsonify({'Estado': 'Salio todo joya'}), 200


app.register_blueprint(item_bp)

if __name__ == '__main__':
    app.run()
