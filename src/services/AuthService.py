from src.database.db_mysql import get_connection;
from src.models.usersModel import Users
from werkzeug.security import check_password_hash

class AuthService():

    @classmethod
    def verificar_identidad(cls, user:Users):
        try:
            connection= get_connection()
            print(connection)
            Authenticated_user= None

            with connection.cursor() as cursor:
                cursor.execute('CALL sp_verificacion_identidad(%s)',user.name_user)
                row= cursor.fetchone()
                print(row)
                print(user.password)

                if(row != None and check_password_hash(row[2], user.password)):
                    Authenticated_user= row
                else:
                    Authenticated_user= None

            connection.close()

            return Authenticated_user
        except Exception as ex:
            print(ex)