from abc import ABCMeta,abstractmethod
class Person(metaclass=ABCMeta):
    @abstractmethod
    def show(self):
        pass
class ManOfPerson(Person):
    def show(self):
        print("man show power")
class WomanOfPerson(Person):
    def show(self):
        print("woman show beautiful")
class ChildOfPerson(Person):
    def show(self):
        print("child show toy")
class Family(metaclass=ABCMeta):
    def __init__(self):
        self.member=[]
        self.createshow()
    @abstractmethod
    def createshow(self):
        pass

    def getmember(self):
        return self.member
    def addmember(self,oneperson):
        self.member.append(oneperson)
class TomFamily(Family):
    def createshow(self):
        self.addmember(ManOfPerson)
        self.addmember(WomanOfPerson)
class JimFamily(Family):
    def createshow(self):
        self.addmember(ManOfPerson)
        self.addmember(ChildOfPerson)
if __name__ == '__main__':
    family_type=eval("TomFamily")()
    print("create show ..",type(family_type).__name__)
    # print("create show ..",family_type.__name__)
    print("family has member--",family_type.getmember())