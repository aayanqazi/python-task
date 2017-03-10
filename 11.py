class Person:

    def getgender(self):
        return "Not Slected Yet"


class Male(Person):
    def getgender(self):
        return "Male"


class Female(Person):
    def getgender(self):
        return "Female"


newUser = Female()

print(newUser.getgender())

newUser1 = Male()

print(newUser1.getgender())

