# Mock Code Challenge - Ramen Shop (Object Relationships)

For this assignment, we'll be working with a Ramen shop-style domain.

We have three models: `Ramen`, `Customer`, and `Order`.

For our purposes, a `Ramen` has many `Order`s, a `Customer` has many
`Order`s, and a `Order` belongs to a `Customer` and to a `Ramen`.

`Ramen` - `Customer` is a many to many relationship.

**Note**: You should draw your domain on paper or on a whiteboard _before you
start coding_. Remember to identify a single source of truth for your data.

## Topics

- Classes and Instances
- Class and Instance Methods
- Variable Scope
- Object Relationships
- lists and list Methods

## Instructions

To get started, run `pipenv install` while inside of this directory.

Build out all of the methods listed in the deliverables. The methods are listed
in a suggested order, but you can feel free to tackle the ones you think are
easiest. Be careful: some of the later methods rely on earlier ones.

**Remember!** This code challenge has tests to help you check your work. You
can run `pytest` to make sure your code is functional before submitting.

We've provided you with a tool that you can use to test your code. To use it,
run `python debug.py` from the command line. This will start a `ipdb` session
with your classes defined. You can test out the methods that you write here. You
can add code to the `debug.py` file to define variables and create sample
instances of your objects.

Writing error-free code is more important than completing all of the
deliverables listed - prioritize writing methods that work over writing more
methods that don't work. You should test your code in the console as you write.

Similarly, messy code that works is better than clean code that doesn't. First,
prioritize getting things working. Then, if there is time at the end, refactor
your code to adhere to best practices. When you encounter duplicated logic,
extract it into a shared helper method.

**Before you submit!** Save and run your code to verify that it works as you
expect. If you have any methods that are not working yet, feel free to leave
comments describing your progress.

## Deliverables

Write the following methods in the classes in the files provided. Feel free to
build out any helper methods if needed.

### Initializers and Properties

#### Customer

- `Customer __init__(self, name)`
  - Customer should be initialized with a name
- `Customer property name`
  - Return name
  - Names must be of type `str`
  - Names must be between 1 and 15 characters, inclusive
  - `raise Exception` if setter fails

#### Ramen

- `Ramen __init__(self, name)`
  - Ramens should be initialized with a name, as a string
- `Ramen property name`
  - Returns the ramen's name
  - Should not be able to change after the ramen is created
  - _hint: `hasattr()`_
  - `raise Exception` if setter fails

#### Order

- `Order __init__(self, customer, ramen, price)`
  - Orders should be initialized with a customer, ramen, and a price (a number)
- `Order property price`
  - Returns the price for a ramen
  - Price must be a number between 1 and 10, inclusive
    - `raise Exception` if setter fails

### Object Relationship Methods and Properties

#### Order

- `Order property customer`
  - Returns the customer object for that order
  - Must be of type `Customer`
  - `raise Exception` if setter fails
- `Order property ramen`
  - Returns the ramen object for that order
  - Must be of type `Ramen`
  - `raise Exception` if setter fails

#### Ramen

- `Ramen orders()`
  - Returns a list of all orders for that ramen
- `Ramen customers(new_customer=None)`
  - if new_customer is of type `Customer`, creates a new order and associates it with that customer (new_customer) and ramen (self). You can enter any integer or float value for the price. 
  - Returns a **unique** list of all customers who have ordered a particular ramen.

#### Customer

- `Customer orders()`
  - Returns a list of all orders a customer has ordered
- `Customer ramens(new_ramen=None)`
  - if new_ramen is of type `Ramen`, creates a new order and associates it with that customer and ramen.
  - Returns a **unique** list of all ramens a customer has ordered

### Aggregate and Association Methods

#### Ramen

- `Ramen num_orders()`
  - Returns the total number of times that ramen has been ordered
- `Ramen average_price()`
  - Returns the average price for a ramen based on its orders
  - Reminder: you can calculate the average by adding up all the orders prices and
    dividing by the number of orders