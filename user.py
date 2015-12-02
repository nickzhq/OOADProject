__author__ = 'Nick'

class user:
    def __init__(self, username , password  ):
        self.__username = username
        self.__password = password
        self.__salary = None

    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self, new ):
        if( new < 0):
            self.__salary = 0
        else:
            self.__salary = new

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, new ):
        self.__password = new

    def view_status(self):
        print(self)

    def __str__(self):
        return str(self.__username+"   "+self.__password + "   " + str(self.__salary))
class manager(user):
    def __init__(self, username, password):
        super().__init__(username, password )

class employee(user):
    def __init__(self, username, password):
        super().__init__(username, password )

