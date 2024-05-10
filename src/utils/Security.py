import datetime
import jwt
import pytz
import uuid
from src.models.usersModel import Users

class Security ():
    jwt_key= "jzajs*!"
    tz= pytz.timezone('UTC')

    @classmethod
    def generate_token(cls, user:Users):
        try:
            #Importamos datetime para el tiempo actual también instalar el de zona hoaria (pip install pytz).
            current_tiem= datetime.datetime.now(tz=cls.tz)

            payload={
                #Identificador único del token
                'jti':str(uuid.uuid4()),
                #Tiempo que fue generado
                'iat': current_tiem,
                #A partir de cuando estará disponible
                'nbf':current_tiem,
                #Fecha de expiración
                'exp':current_tiem+datetime.timedelta(minutes=30),
                #Datos
                'id_user': user.id_user,
                'name_user': user.person.name_person,
                'id_rol': user.usertype.id_usertype,
                'name_rol': user.usertype.nombre_usertype
            }

            return jwt.encode(payload, cls.jwt_key, algorithm="HS256")
        
        except Exception as ex:
            print(ex)