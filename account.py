#This file is part pyme module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.
from trytond.model import ModelView, ModelSQL, ModelSingleton, fields
from trytond.pool import Pool
from trytond.transaction import Transaction
from trytond.pyson import Eval, Bool


class Configuration(ModelSingleton, ModelSQL, ModelView):
    _name = 'account.configuration'

    default_customer_tax = fields.Property(
        fields.Many2One('account.tax', 'Default Customer Tax'))
    default_supplier_tax = fields.Property(
        fields.Many2One('account.tax', 'Default Supplier Tax'))

Configuration()
