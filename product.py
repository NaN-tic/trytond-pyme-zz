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
