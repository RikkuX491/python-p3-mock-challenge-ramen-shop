from classes.customer import Customer
from classes.ramen import Ramen

class Order:

    all = []

    def __init__(self, customer, ramen, price):
        self.customer = customer
        self.ramen = ramen
        self.price = price
        Order.all.append(self)

    def get_customer(self):
        return self._customer
    
    def set_customer(self, customer):
        if(type(customer) == Customer):
            self._customer = customer
        else:
            raise Exception("customer must be of type Customer!")
        
    def get_ramen(self):
        return self._ramen
    
    def set_ramen(self, ramen):
        if(type(ramen) == Ramen):
            self._ramen = ramen
        else:
            raise Exception("ramen must be of type Ramen!")

    customer = property(get_customer, set_customer)
    ramen = property(get_ramen, set_ramen)