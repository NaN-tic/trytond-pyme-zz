# This file is part pyme module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['AccountConfiguration', 'TaxLine']


class AccountConfiguration:
    __metaclass__ = PoolMeta
    __name__ = 'account.configuration'
    description_for_account_move_line = fields.Selection([
            ('description', 'Invoice Description'),
            ('reference', 'Invoice Reference'),
            ('reference_description',
                'Invoice Description and Reference'),
            ], 'Description for Invoice Account Move Line')

    @staticmethod
    def default_description_for_account_move_line():
        return 'reference_description'


class TaxLine:
    __metaclass__ = PoolMeta
    __name__ = 'account.tax.line'

    def on_change_tax(self):
        super(TaxLine, self).on_change_tax()
        self.code = None

    @fields.depends('move_line')
    def on_change_with_company(self, name=None):
        return super(TaxLine, self).on_change_with_company(name)
