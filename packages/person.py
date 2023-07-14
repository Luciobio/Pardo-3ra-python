class Person:
    def __init__(self, name, lastName, bornIn):
        self.name = name
        self.lastName = lastName
        self.bornIn = bornIn

    def __str__(self):
        return (
            "Name: "
            + self.name
            + " "
            + self.lastName
            + ", Born in: "
            + str(self.bornIn)
        )
