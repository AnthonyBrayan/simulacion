from src.database.db_mysql import get_connection;
from src.models.usersModel import Users
from src.models.PersonModel import Person
from src.models.usertypeModel import UserType
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
                    person = Person(row[3],row[4],row[5],row[6])
                    usertype = UserType(row[7],row[8])

                    Authenticated_user= Users(row[0],row[1],row[2],person,usertype)
                    
                else:
                    Authenticated_user= None

            connection.close()

            return Authenticated_user
        except Exception as ex:
            print(ex)