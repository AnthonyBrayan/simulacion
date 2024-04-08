from src.database.db_mysql import get_connection;
from src.models.usersModel import Users;
from werkzeug.security import generate_password_hash

class UsersService():

    @classmethod
    def get_user(cls):
        try:
            connection= get_connection()
            print(connection)

            with connection.cursor() as cursor:
                cursor.execute('CALL sp_consutarusuarios ()')
                result= cursor.fetchall()
                print(result)

            connection.close()
            return 'Este es el método get, se imprime en consola, hola'
        except Exception as ex:
            print(ex)

    @classmethod
    def post_user(cls,user: Users):
        try:
            connection= get_connection()
            print(connection)
            with connection.cursor() as cursor:
                id_user= user.id_user
                nameUser = user.name_user
                password = user.password
                id_usertype = user.usertype
                id_person= user.person

                encripted_password = generate_password_hash(password,'pbkdf2:sha256',30)

                cursor.execute("INSERT INTO users (id_users ,name_user, password, id_person , id_usertype ) "+
                "VALUES ({0}, '{1}', '{2}', {3}, {4});".format(id_user,nameUser,encripted_password,id_person,id_usertype))
                connection.commit()

            connection.close()

            return 'Este es el método get, se imprime en consola'
        except Exception as ex:
            print(ex)

    @classmethod
    def put_user(cls,user: Users):
            try:
                connection= get_connection()
                print(connection)
                with connection.cursor() as cursor:
                 id_user= user.id_user
                 nameUser = user.name_user
                 password = user.password
                 id_person= user.person
                 id_usertype = user.usertype

                 cursor.execute("UPDATE users SET name_user = '{0}', password = '{1}', id_person = {2}, id_usertype = {3} WHERE users.id_users = {4};".format(nameUser,password,id_person,id_usertype,id_user))
                 connection.commit()

                connection.close()

                return 'Este es el método put, se imprime en consola'
            except Exception as ex:
                print(ex)

    @classmethod
    def delete_user(cls,id_user: int):
            try:
                connection= get_connection()
                print(connection)
                with connection.cursor() as cursor:

                    cursor.execute("CALL sp_deleteUser(%s)",id_user)
                    connection.commit()
                    
                connection.close()

                return 'Este es el método delete, se imprime en consola'
            except Exception as ex:
                print(ex)


