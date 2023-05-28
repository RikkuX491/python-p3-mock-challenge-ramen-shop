from classes.customer import Customer
from classes.ramen import Ramen

class Order:

    def __init__(self, customer, ramen, price):
        self.customer = customer
        self.ramen = ramen
        self.price = price