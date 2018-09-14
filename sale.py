# This file is part pyme module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import PoolMeta
from trytond.model import fields
from trytond.pyson import Eval, If, Equal

__all__ = ['Sale', 'SaleLine']


class Sale:
    __metaclass__ = PoolMeta
    __name__ = 'sale.sale'
    email = fields.Function(fields.Char('E-mail'), 'get_email')

    def get_email(self, name):
        return self.party.email if self.party else None

    @classmethod
    def view_attributes(cls):
        return super(Sale, cls).view_attributes() + [
            ('/tree', 'colors',
                If(Equal(Eval('state'), 'draft'), 'blue',
                If(Equal(Eval('state'), 'quotation'), 'darkgreen',
                If(Equal(Eval('state'), 'confirmed'), 'brown',
                If(Equal(Eval('shipment_state'), 'exception'), 'red',
                If(Equal(Eval('invoice_state'), 'exception'), 'red',
                If(Equal(Eval('state'), 'cancel'), 'grey', 'black')))))),
                )]


class SaleLine:
    __metaclass__ = PoolMeta
    __name__ = 'sale.line'

    def on_change_product(self):
        super(SaleLine, self).on_change_product()
        if not self.product:
            self.description = None
