import pytest

from classes.ramen import Ramen
from classes.customer import Customer
from classes.order import Order

class TestCustomer:
    '''Customer in customer.py'''

    def test_has_name(self):
        '''customer is initialized with name'''
        customer = Customer('Steve')
        assert (customer.name == "Steve")

    def test_can_change_name(self):
        '''customer name can be changed'''
        customer = Customer('Steve')
        customer.name = "Stove"
        assert (customer.name == "Stove")

    def test_customer_name_is_str(self):
        '''customer name is a string'''
        customer = Customer('Steve')
        assert (isinstance(customer.name, str))

        with pytest.raises(Exception):
            customer.name = 1

    def test_customer_name_length(self):
        '''customer name is between 1 and 15 characters'''
        customer = Customer('Steve')
        assert (len(customer.name) == 5)

        with pytest.raises(Exception):
            customer.name = "NameLongerThan15Characters"

        with pytest.raises(Exception):
            customer.name = ""

    def test_has_many_orders(self):
        '''customer has many orders'''
        ramen = Ramen("Shoyu ramen")
        customer = Customer('Steve')
        customer_2 = Customer('Dima')
        order_1 = Order(customer, ramen, 2)
        order_2 = Order(customer, ramen, 5)
        order_3 = Order(customer_2, ramen, 5)

        assert (len(customer.orders()) == 2)
        assert (not order_3 in customer.orders())
        assert (order_1 in customer.orders())
        assert (order_2 in customer.orders())

    def test_orders_of_type_order(self):
        '''customer orders are of type Order'''
        ramen = Ramen("Shoyu ramen")
        customer = Customer('Steve')
        order_1 = Order(customer, ramen, 2)
        order_2 = Order(customer, ramen, 5)

        assert (isinstance(customer.orders()[0], Order))
        assert (isinstance(customer.orders()[1], Order))

    def test_has_many_ramens(self):
        '''customer has many ramens.'''
        ramen = Ramen("Shoyu ramen")
        ramen_2 = Ramen("Miso ramen")

        customer = Customer('Steve')
        order_1 = Order(customer, ramen, 2)
        order_2 = Order(customer, ramen_2, 5)

        assert (ramen in customer.ramens())
        assert (ramen_2 in customer.ramens())

    def test_has_unique_ramens(self):
        '''customer has unique list of all the ramens they have ordered.'''
        ramen = Ramen("Shoyu ramen")
        ramen_2 = Ramen("Miso ramen")

        customer = Customer('Steve')
        order_1 = Order(customer, ramen, 2)
        order_2 = Order(customer, ramen, 2)
        order_3 = Order(customer, ramen_2, 5)

        assert (len(set(customer.ramens())) == len(customer.ramens()))
        assert (len(customer.ramens()) == 2)
