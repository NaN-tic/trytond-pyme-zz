# This file is part pyme module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import PoolMeta
from trytond.model import fields

__all__ = ['ProductCategory', 'ProductTemplate']
__metaclass__ = PoolMeta


class ProductCategory:
    __name__ = 'product.category'
    accounting = fields.Boolean('Accounting', select=True)


class ProductTemplate:
    __name__ = 'product.template'
    account_category_migration = fields.Many2One('product.category', 'Account Category',
        domain=[
            ('accounting', '=', True),
            ])
