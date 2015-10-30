__author__ = 'Nick'

class item:
    ''' record the info of item
    '''
    def __init__( self,name = None, price = None, exp_date = None, quantity = None ):
        '''
        If no parameter, all variable is set to None
        :param name: name of item
        :param price: price of item
        :param exp_date: expiration date of item
        :param quantity: numbers of item
        '''
        self.__name = name
        self.__price = price
        self.__exp_date = exp_date
        self.__quantity = quantity
    def set_name(self, name):
        '''
        set name
        '''
        self.__name = name
    def set_price(self, price):
        ''' set price
        :param price:
        '''
        self.__price = price
    def set_exp_date(self, exp_date):
        ''' set expiration date
        :param exp_date:
        '''
        self.__exp_date = exp_date
    def set_quantity(self, quantity):
        ''' set quantity
        :param quantity:
        '''
        self.__quantity = quantity
    def name(self):
        return self.__name
    def price(self):
        return self.__price
    def exp_date(self):
        return self.__exp_date
    def quantity(self):
        return self.__quantity
