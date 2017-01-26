# This file is part pyme module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool, PoolMeta

__all__ = ['ProductTemplate']


class ProductTemplate:
    __metaclass__ = PoolMeta
    __name__ = 'product.template'

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
