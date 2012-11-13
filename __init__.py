#This file is part pyme module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.

from trytond.pool import Pool
from .account import *
from .bank import *
# from .party import *
from .product import *
from .sale import *

def register():
    Pool.register(
        AccountConfiguration,
        BankAccount,
        # Party,
        ProductTemplate,
        SaleConfiguration,
        module='pyme', type_='model')
