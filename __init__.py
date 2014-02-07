#This file is part pyme module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.pool import Pool
from .account import *
from .bank import *
from .product import *
from .attachment import *


def register():
    Pool.register(
        AccountConfiguration,
        BankAccount,
        ProductTemplate,
        Attachment,
        module='pyme', type_='model')
