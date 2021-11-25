"""
uses OOP + pickle module to implement permanent storage of files (as binary files) and allows for retrieval + update
"""

import pickle
class Pickles:
    def __init__(self,vegetal,container,sour,tang):
        self.__vegetal = vegetal
        self.__container = container
        self.__pickledays = 0
        self.__sour = sour
        self.__tang = tang

    def admirePickle(self):
        print("vegetal:", self.__vegetal)
        print("container:",self.__container)
        print("pickled for:",self.__pickledays,"days")
        print("sourness:", self.__sour)
        print("tanginess:",self.__tang)

    def changeContainer(self, newcontainer):
        self.__container = newcontainer

    def updateSour(self, newsour):
        self.__sour = newsour

    def updateTang(self, newtang):
        self.__tang = newtang

    def agePickle(self):
        self.__pickledays += 1

class Database():
    def MakePickle(self):
        vegetal = input("What vegetable?")
        container = input("What container?")
        sour = int(input("How sour?"))
        tang = int(input("How tangy"))
        name = input("Name your pickle:")
        object = Pickles(vegetal, container, sour, tang)
        file = open(name,'wb')
        pickle.dump(object,file)
        file.close()

    def OpenPickleJar(self, name):
        name = input("What's your pickle name?")
        file = open(name,'rb')
        pickleobject = pickle.load(file)
        file.close()
        pickleobject.admirePickle()
        return pickleobject

def Main():
    database = Database()
    while True:
        print("1: make a new pickle")
        print("2: view a pickle")
        print("3: update pickle stats")
        choice = int(input("so?"))
        if choice == 1:
            database.MakePickle()
        elif choice == 2:
            name = input("What's your pickle name?")
            database.OpenPickleJar()
        elif choice == 3:
            name = input("What's your pickle name?")
            pickle = database.OpenPickleJar()
            update = input("select what to update")
            if update == "container":
                container = input("input new container:")
                pickle.changeContainer(container)
            elif update == "sourness":
                sourlevel = input("update sourness:")
                pickle.updateSour(sourlevel)
            elif update == "tanginess":
                tanglevel = input("update tanginess"):
                pickle.updateTang(tanglevel)
            file = open(name, 'wb')
            pickle.dump(pickle,file)
            file.close()
                
