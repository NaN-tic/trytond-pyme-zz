#This file is part pyme module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.
from trytond.model import ModelView, ModelSQL, ModelSingleton, fields
from trytond.pool import Pool, PoolMeta
from trytond.transaction import Transaction
from trytond.pyson import Eval, Bool

__all__ = ['AccountConfiguration']
__metaclass__ = PoolMeta

class AccountConfiguration(ModelSingleton, ModelSQL, ModelView):
    __name__ = 'account.configuration'

    default_customer_tax = fields.Property(
        fields.Many2One('account.tax', 'Default Customer Tax'))
    default_supplier_tax = fields.Property(
        fields.Many2One('account.tax', 'Default Supplier Tax'))

