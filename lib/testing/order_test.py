from classes.ramen import Ramen
from classes.customer import Customer
from classes.order import Order
import pytest


class TestOrders:
    '''Order in order.py'''

    def test_has_price(self):
        '''is initialized with a price'''
        ramen = Ramen("Shoyu ramen")
        customer = Customer('Steve')
        order_1 = Order(customer, ramen, 2)
        order_2 = Order(customer, ramen, 5)

        assert (order_1.price == 2)
        assert (order_2.price == 5)

    def test_has_a_customer(self):
        '''order has a customer .'''
        ramen = Ramen("Shoyu ramen")
        customer_1 = Customer('Wayne')
        customer_2 = Customer('Dima')
        order_1 = Order(customer_1, ramen, 2)
        order_2 = Order(customer_2, ramen, 5)

        assert (order_1.customer == customer_1)
        assert (order_2.customer == customer_2)

    def test_customer_of_type_customer(self):
        '''customer is of type Customer'''
        ramen = Ramen("Shoyu ramen")
        customer = Customer('Steve')
        order_1 = Order(customer, ramen, 2)
        order_2 = Order(customer, ramen, 5)

        assert (isinstance(order_1.customer, Customer))
        assert (isinstance(order_2.customer, Customer))

    def test_has_a_ramen(self):
        '''Review has a ramen.'''
        ramen_1 = Ramen("Shoyu ramen")
        ramen_2 = Ramen("Miso ramen")
        customer = Customer('Wayne')
        order_1 = Order(customer, ramen_1, 2)
        order_2 = Order(customer, ramen_2, 5)

        assert (order_1.ramen == ramen_1)
        assert (order_2.ramen == ramen_2)

    def test_ramen_of_type_ramen(self):
        '''ramen is of type Ramen'''
        ramen = Ramen("Shoyu ramen")
        customer = Customer('Steve')
        order_1 = Order(customer, ramen, 2)
        order_2 = Order(customer, ramen, 5)

        assert (isinstance(order_1.ramen, Ramen))
        assert (isinstance(order_2.ramen, Ramen))

    def test_get_all_orders(self):
        '''test Order class all attribute'''
        Order.all = []
        ramen = Ramen("Shoyu ramen")
        customer = Customer('Wayne')
        customer_2 = Customer('Dima')
        order_1 = Order(customer, ramen, 2)
        order_2 = Order(customer_2, ramen, 5)

        assert (len(Order.all) == 2)
        assert (order_1 in Order.all)
        assert (order_2 in Order.all)
