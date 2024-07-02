from flask import Blueprint,session
from todor.auth import loginrequired
bp = Blueprint('todo',__name__,url_prefix='/todo')


@bp.route('/list')
@loginrequired
def index():
    return "Lista de tareas"

@bp.route('/create')
def create():
    return "Crear tarea"
