# Ventu test - exercise 2
class customerPerson:
    def __init__(self, id, firstname, lastname, country, creditLimit):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.country = country
        self.creditLimit = creditLimit

customers = []

customers.append(customerPerson(1, "Alex", "White", "USA", 200350))
customers.append(customerPerson(2, "Tyler", "Hanson", "UK", 200350))
customers.append(customerPerson(3, "Jordan", "Fernandez", "France", 200350))
customers.append(customerPerson(4, "Drew", "Bradley", "Albania", 200350))
customers.append(customerPerson(5, "Blake", "Fuller", "USA", 200350))
customers.append(customerPerson(6, "Spencer", "Johnston", "China", 200350))
customers.append(customerPerson(7, "Ellis", "Gutierrez", "USA", 200350))
customers.append(customerPerson(8, "Morgan", "Thomas", "Canada", 200350))
customers.append(customerPerson(9, "Riley", "Garza", "UK", 200350))
customers.append(customerPerson(10, "Peyton", "Harris", "USA", 200350))

filteredCustomers = []

for customer in customers:
    names = []
    names.append(customer.firstname)
    names.append(customer.lastname)
    if (len(''.join(names)) < 12):
        filteredCustomers.append(customer)

sortedCustomers = []
sortedArr = []
for unsorted in filteredCustomers:  
    names = []
    names.append(unsorted.firstname)
    names.append(unsorted.lastname)
    sortedArr.append(''.join(names))

sortedCustomers = sorted(sortedArr, key=len)

for ord in sortedCustomers:
    for customer in customers:
        if (customer.firstname + customer.lastname == ord):
            print(customer.id, customer.firstname, customer.lastname)