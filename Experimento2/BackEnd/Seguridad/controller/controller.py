from flask import request
from ..model import db, Usuario, Rol, UsuarioSchema
from flask_restful import Resource
from ..client import Client
from ..sender import sender
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from datetime import datetime

client = Client()
usuario_schema = UsuarioSchema()

class ControllerLogIn(Resource):

    def post(self):
        usuario = Usuario.query.filter(Usuario.nombre == request.json["nombre"], Usuario.contrasena == request.json["contrasena"]).first()
        db.session.commit()
        if usuario is None:
            return "El usuario no existe", 404
        else:
            ## TODO - Llamado a servicio de traza
            ## client.executeClient(usuario)
            now = datetime.now()
            date = now.strftime("%d/%m/%Y %H:%M:%S")
            ## TODO - Envio Email
            sender.send_email(usuario.nombre,request.remote_addr,str(request.user_agent),date)
            token_de_acceso = create_access_token(identity = usuario.id)
            return {"mensaje":"Inicio de sesión exitoso", "token": token_de_acceso}

class ControllerService(Resource):

    @jwt_required()
    def post(self):
        user_id = get_jwt_identity()
        usuario = Usuario.query.filter(Usuario.id == user_id).first()
        if usuario.rol == Rol.DIRECTOR:
            return 'Respuesta Ok Servicio', 200
        else:
            return 'El Rol no esta Autorizado', 401
