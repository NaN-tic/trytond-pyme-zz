# This file is part pyme module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from .account import *
from .attachment import *
from .bank import *
from .company import *
from .invoice import *
from .move import *
from .product import *
from .purchase import *
from .sale import *
from .shipment import *
from .tax import *

def register():
    Pool.register(
        AccountConfiguration,
        Attachment,
        BankAccount,
        Employee,
        Invoice,
        InvoiceLine,
        Move,
        TaxLine,
        ProductCategory,
        ProductTemplate,
        Purchase,
        Sale,
        ShipmentIn,
        ShipmentInReturn,
        ShipmentInternal,
        ShipmentOut,
        ShipmentOutReturn,
        module='pyme', type_='model')
