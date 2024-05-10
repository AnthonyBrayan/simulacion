class Users():
    def __init__(self,id_user,name_user,password,person,usertype) -> None:
        self.id_user=id_user
        self.name_user=name_user
        self.password = password
        self.person = person
        self.usertype = usertype

    def to_json(self):
        return{
            'id':self.id_user,
            'lasname':self.name_user,
            'password':self.password,
            'person':self.person,
            'userType':self.usertype
        }