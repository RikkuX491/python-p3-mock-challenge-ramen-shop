import pytest

from classes.ramen import Ramen
from classes.customer import Customer
from classes.order import Order

class TestRamen:
    '''Ramen in ramen.py'''

    def test_has_name(self):
        '''ramen is initialized with a name'''
        ramen = Ramen("Shoyu ramen")
        assert (ramen.name == "Shoyu ramen")

    def test_name_is_string(self):
        '''ramen is initialized with a name of type str'''
        ramen = Ramen("Shoyu ramen")
        assert (isinstance(ramen.name, str))

    def test_name_setter(self):
        '''Cannot change the name of the ramen'''
        ramen = Ramen("Shoyu ramen")

        with pytest.raises(Exception):
            ramen.name = "Miso ramen"

    def test_has_many_orders(self):
        '''ramen has many orders.'''
        ramen = Ramen("Shoyu ramen")
        ramen_2 = Ramen("Miso ramen")
        customer = Customer('Steve')
        order_1 = Order(customer, ramen, 2)
        order_2 = Order(customer, ramen, 5)
        order_3 = Order(customer, ramen_2, 5)

        assert (len(ramen.orders()) == 2)
        assert (order_1 in ramen.orders())
        assert (order_2 in ramen.orders())
        assert (not order_3 in ramen.orders())

    def test_orders_of_type_order(self):
        '''ramen orders are of type Order'''
        ramen = Ramen("Shoyu ramen")
        customer = Customer('Steve')
        order_1 = Order(customer, ramen, 2)
        order_2 = Order(customer, ramen, 5)

        assert (isinstance(ramen.orders()[0], Order))
        assert (isinstance(ramen.orders()[1], Order))

    def test_has_many_customers(self):
        '''ramen has many customers.'''
        ramen = Ramen("Shoyu ramen")

        customer = Customer('Steve')
        customer_2 = Customer('Dima')
        order_1 = Order(customer, ramen, 2)
        order_2 = Order(customer_2, ramen, 5)

        assert (customer in ramen.customers())
        assert (customer_2 in ramen.customers())

    def test_has_unique_customers(self):
        '''ramen has unique list of all the customers that have ordered it.'''
        ramen = Ramen("Shoyu ramen")

        customer = Customer('Steve')
        customer_2 = Customer('Dima')
        order_1 = Order(customer, ramen, 2)
        order_2 = Order(customer_2, ramen, 2)
        order_3 = Order(customer, ramen, 5)

        assert (len(set(ramen.customers())) == len(ramen.customers()))
        assert (len(ramen.customers()) == 2)

    def test_customers_of_type_customer(self):
        '''ramen customers are of type Customer'''
        ramen = Ramen("Shoyu ramen")
        customer = Customer('Steve')
        customer_2 = Customer('Dima')
        order_1 = Order(customer, ramen, 2)
        order_2 = Order(customer_2, ramen, 5)

        assert (isinstance(ramen.customers()[0], Customer))
        assert (isinstance(ramen.customers()[1], Customer))

    def test_get_number_of_orders(self):
        '''test num_orders()'''
        ramen = Ramen("Shoyu ramen")
        customer = Customer('Steve')
        order_1 = Order(customer, ramen, 2)
        order_2 = Order(customer, ramen, 5)

        assert (ramen.num_orders() == 2)

    def test_average_price(self):
        '''test average_price()'''
        ramen = Ramen("Shoyu ramen")
        customer = Customer('Steve')
        customer_2 = Customer('Dima')
        Order(customer, ramen, 2)
        Order(customer_2, ramen, 5)

        assert (ramen.average_price() == 3.5)
