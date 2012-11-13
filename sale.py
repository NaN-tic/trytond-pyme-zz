#This file is part pyme module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta
from trytond.pyson import Eval

__all__ = ['SaleConfiguration']
__metaclass__ = PoolMeta

class SaleConfiguration:
    'Sale Configuration'
    __name__ = 'sale.configuration'
    sale_price_list = fields.Property(fields.Many2One('product.price_list',
            'Sale Price List',
            domain=[
                ('company', '=', Eval('context', {}).get('company')),
                ],
            states={
                'invisible': ~Eval('context', {}).get('company'),
                }))
