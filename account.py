# This file is part pyme module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import ModelView, ModelSQL, ModelSingleton, fields
from trytond.pool import PoolMeta

__all__ = ['AccountConfiguration']
__metaclass__ = PoolMeta


class AccountConfiguration(ModelSingleton, ModelSQL, ModelView):
    __name__ = 'account.configuration'
    default_customer_tax = fields.Property(
        fields.Many2One('account.tax', 'Default Customer Tax',
        domain=[
            ('parent', '=', None),
            ('group.kind', 'in', ['sale', 'both']),
            ]))
    default_supplier_tax = fields.Property(
        fields.Many2One('account.tax', 'Default Supplier Tax',
        domain=[
            ('parent', '=', None),
            ('group.kind', 'in', ['purchase', 'both']),
            ]))
    description_for_account_move_line = fields.Selection([
            ('description', 'Invoice Description'),
            ('reference', 'Invoice Reference'),
            ('reference+description',
                'Invoice Description Plus Reference'),
            ], 'Description for Invoice Account Move Line')

    @classmethod
    def default_description_for_account_move_line(cls):
        return 'invoice_description'
