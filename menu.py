from packages.customer import Customer

first = str(input("First name: "))
last = str(input("Last name: "))
year = int(input("Born in (year): "))
mail = str(input("E-mail: "))

customer1 = Customer(first, last, year, mail)

print(customer1)