# This file is part pyme module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['TaxLine']
__metaclass__ = PoolMeta


class TaxLine():
    __name__ = 'account.tax.line'

    def on_change_tax(self):
        super(TaxLine, self).on_change_tax()
        self.code = None

    @fields.depends('move_line')
    def on_change_with_company(self, name=None):
        return super(TaxLine, self).on_change_with_company(name)
