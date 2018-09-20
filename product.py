# This file is part pyme module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool, PoolMeta
from trytond.model import fields

__all__ = ['ProductCategory', 'ProductTemplate']


class ProductCategory:
    __name__ = 'product.category'
    accounting = fields.Boolean('Accounting', select=True)



class ProductTemplate:
    __metaclass__ = PoolMeta
    __name__ = 'product.template'
    account_category_migration = fields.Many2One('product.category', 'Account Category',
        domain=[
            ('accounting', '=', True),
            ])

    @staticmethod
    def default_accounts_category():
        return True

    @staticmethod
    def default_taxes_category():
        return True

    @staticmethod
    def default_customer_taxes():
        Config = Pool().get('account.configuration')
        customer_tax = Config(1).customer_tax
        if customer_tax:
            return [customer_tax.id]

    @staticmethod
    def default_supplier_taxes():
        Config = Pool().get('account.configuration')
        supplier_tax = Config(1).supplier_tax
        if supplier_tax:
            return [supplier_tax.id]
