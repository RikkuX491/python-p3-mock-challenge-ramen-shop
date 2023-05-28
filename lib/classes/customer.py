class Customer:

    all = []

    def __init__(self, name):
        self.name = name
        Customer.all.append(self)
        
    def orders(self):
        from classes.order import Order
        return [order for order in Order.all if order.customer is self]
    
    def ramens(self, new_ramen=None):
        from classes.ramen import Ramen
        from classes.order import Order
        if(type(new_ramen) == Ramen):
            Order(self, new_ramen, 8.99)
        return list(set([order.ramen for order in Order.all if order.customer is self]))

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if(type(name) == str) and (1 <= len(name) <= 15):
            self._name = name
        else:
            raise Exception("Invalid name!")

    name = property(get_name, set_name)