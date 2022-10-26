from DAL.adressDAL import AddressDAL
from DAL.personDAL import PersonDAL
from DAL.phonesDAL import PhonsDAL

class UsersBLL:
    def __init__ (self):
        self.__persons=PersonDAL().get_persons()
        self.__address=AddressDAL().get__collection()
        self.__phones=PhonsDAL().get_phons()
        self.users=[]
    def get_users(self):
        
        for  i in range(len(self.__address)):
            phones=next(item for item in self.__phones if item["id"] ==  self.__address[i]["extenarlId"])
            persons=next(item for item in self.__persons if item["id"] ==  self.__address[i]["extenarlId"])
            user={
                "id":i+1,
                "name":persons["name"],
                "email":persons["email"],
                "phone":phones["phone"],
                "address":{"country":self.__address[i]['country']
                ,"city":self.__address[i]['city']
                }
            }
            
            self.users.append(user)
        return self.users
    def printPerson(self):
        print(self.__address[1]["country"])


