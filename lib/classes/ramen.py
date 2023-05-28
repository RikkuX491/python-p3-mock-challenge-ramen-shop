class Ramen:

    all = []

    def __init__(self, name):
        self.name = name
        Ramen.all.append(self)
        
    def orders(self):
        from classes.order import Order
        return [order for order in Order.all if order.ramen is self]
    
    def customers(self, new_customer=None):
        from classes.customer import Customer
        from classes.order import Order
        if(type(new_customer) == Customer):
            Order(new_customer, self, 5.99)
        return list(set([order.customer for order in Order.all if order.ramen is self]))
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        prices = [order.price for order in self.orders()]
        return sum(prices) / len(prices)

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        if(not hasattr(self, 'name')) and (type(name) == str):
            self._name = name
        else:
            raise Exception("Invalid name or cannot change name!")

    name = property(get_name, set_name)