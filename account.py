#This file is part pyme module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.model import ModelView, ModelSQL, ModelSingleton, fields
from trytond.pool import PoolMeta

__all__ = ['AccountConfiguration']
__metaclass__ = PoolMeta


class AccountConfiguration(ModelSingleton, ModelSQL, ModelView):
    __name__ = 'account.configuration'
    default_customer_tax = fields.Property(
        fields.Many2One('account.tax', 'Default Customer Tax',
        domain=[
            ('group.kind', 'in', ['sale', 'both']),
            ]))
    default_supplier_tax = fields.Property(
        fields.Many2One('account.tax', 'Default Supplier Tax',
        domain=[
            ('group.kind', 'in', ['purchase', 'both']),
            ]))
