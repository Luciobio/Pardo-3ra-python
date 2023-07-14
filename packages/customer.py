import datetime
from packages.person import Person

year = datetime.date.today().year


class Customer(Person):
    def __init__(self, name, lastName, bornIn, email):
        super().__init__(name, lastName, bornIn)
        self.__email = email
        self.age = year - bornIn
        self.active = True

    def get_email(self):
        return "E-mail: " + str(self.__email)

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def __str__(self):
        return (
            super().__str__()
            + ", Age: "
            + str(self.age)
            + ", "
            + self.get_email()
            + ", Active: "
            + str(self.active)
        )

