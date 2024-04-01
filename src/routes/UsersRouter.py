from flask import Blueprint, request

from src.services.UsersService import UsersService
from src.models.usersModel import Users

main = Blueprint('users_blueprint',__name__)

# @main.route('/',methods=['GET','POST'])
# def get_users():

#     nameUser = request.json['nameuser']
#     password= request.json['password']
#     idUserType = request.json['id_usertype']
#     idPerson = request.json['id_person']

#     user = Users(0,nameUser,password,idUserType,idPerson)

#     if request.method == 'GET':
#         get_user=UsersService.get_user()
#         print(get_user)

#     elif request.method == 'POST':
#         post_user=UsersService.post_user(user)
#         print(post_user)

#     return 'Esto se ve en la página'

@main.route('/',methods=['GET'])
def get_users():

    get_user=UsersService.get_user()
    print(get_user)

    return 'Esto se ve en la página, GET'

@main.route('/post',methods=['POST'])
def post_users():

    nameUser = request.json['nameuser']
    password= request.json['password']
    idPerson = request.json['id_person']
    idUserType = request.json['id_usertype']


    user = Users(0,nameUser,password,idPerson,idUserType)

    post_user=UsersService.post_user(user)
    print(post_user)

    return 'Esto se ve en la página, POST'

@main.route('/put',methods=['PUT'])
def put_users():


    id_user = request.json['id_user']
    nameUser = request.json['nameuser']
    password= request.json['password']
    idPerson = request.json['id_person']
    idUserType = request.json['id_usertype']

    user = Users(id_user,nameUser,password,idPerson,idUserType)

    put_user=UsersService.put_user(user)
    print(put_user)

    return 'Esto se ve en la página, Put'

@main.route('/delete',methods=['DELETE'])
def delete_users():

    id_user = request.json['id_user']

    delete_user=UsersService.delete_user(id_user)
    print(delete_user)

    return 'Esto se ve en la página, DELETE'
