""" Optional questions for Lab 8 """



def tax(shopping_cart, percent):
    """ Returns a new list where a `percent` tax is added to each item's price in a shopping cart.
    >>> fruit_cart = [("apple", 0.5, 3), ("banana", 0.25, 4)]
    >>> tax(fruit_cart, 10)
    [('apple', 0.55, 3), ('banana', 0.275, 4)]
    >>> cal_cart = [("oski", 1000, 1), ("go", 1.25, 2), ("bears", 3.5, 2)]
    >>> tax(cal_cart, 100)
    [('oski', 2000.0, 1), ('go', 2.5, 2), ('bears', 7.0, 2)]
    """
    update = []
    for e in shopping_cart:
        update.append(list(e))
    for i in update:
        i[1] = (1 + percent/100) * i[1]
    present = []
    for _ in update:
        present.append(tuple(_))  
    return present
        

    
        
import functools    

def total_cost(shopping_cart):
    """ Returns a float that is the total cost of all items in the shopping cart.
    >>> fruit_cart = [("apple", 0.5, 3), ("banana", 0.25, 4)]
    >>> taxed_fruit = tax(fruit_cart, 10)
    >>> total_cost(taxed_fruit)
    2.75
    >>> cal_cart = [("oski", 1000, 1), ("go", 1.25, 2), ("bears", 3.5, 2)]
    >>> taxed_cart = tax(cal_cart, 100)
    >>> total_cost(taxed_cart)
    2019.0
    """
    total = []
    for item in shopping_cart:
        total.append(item[1]*item[2])
    return functools.reduce(lambda a, b: a+b, total)
    

