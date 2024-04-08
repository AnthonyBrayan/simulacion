from flask import Blueprint, jsonify,request
from src.utils.Security import Security
from src.models.usersModel import Users

from src.services.AuthService import AuthService

main = Blueprint('login_blueprint',__name__)

@main.route('/',methods=['POST'])
def login_users():

    nameUser = request.json['nameuser']
    password= request.json['password']

    user = (Users(0,nameUser,password,None,None))

    Authenticated_user= AuthService.verificar_identidad(user)
    print(Authenticated_user)

    if(Authenticated_user != None):
        encode_toke= Security.generate_token(Authenticated_user)
        return jsonify({'success':True, 'token':encode_toke})
    else:
        return jsonify({'success':False})