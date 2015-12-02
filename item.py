__author__ = 'Nick'

class item:
    ''' record the info of item '''
    def __init__( self,name = None, saleprice = None,original_price = None  ,month = None, quantity = None ):
        '''
        If no parameter, all variable is set to None
        :param name: name of item
        :param saleprice: price of item
        :param month: expiration date of item
        :param quantity: numbers of item
        '''
        self.__name = name
        self.__saleprice = saleprice
        self.__month = month
        self.__quantity = quantity
        self.__original_price = original_price

    @property
    def original_price(self):
        return self.__original_price
    @original_price.setter
    def original_price(self, original_price):
        if( original_price < 0 ):
            self.__original_price = 0
        else:
            self.__original_price = original_price

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def saleprice(self):
        return self.__saleprice
    @saleprice.setter
    def saleprice(self, saleprice):
        if (saleprice < 0):
            self.__saleprice = 0
        else:
            self.__saleprice = saleprice

    @property
    def month(self):
        return self.__month
    @month.setter
    def month(self, month):
        if( month >=1 & month <=12 ):
            self.__month = month
        else:
            self.__month = 1

    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, quantity):
        if( quantity < 0 ):
            self.__quantity = 0
        else:
            self.__quantity = quantity

    def __str__(self):
        return ("Name:"+self.__name + " Sale_Price:" + str(self.__saleprice) + " Original_Price:"+ str(self.__original_price) +" Incoming_Month:"+str( self.__month) + " Quantity:" + str(self.__quantity))
