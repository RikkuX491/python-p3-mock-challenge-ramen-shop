class Customer:
    def __init__(self, name):
        self.name = name
        
    def orders(self):
        from classes.order import Order
        pass
    
    def ramens(self, new_ramen=None):
        from classes.ramen import Ramen
        from classes.order import Order
        pass