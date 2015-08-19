# This file is part pyme module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import PoolMeta
from trytond.pyson import Eval, If, Equal

__all__ = ['Sale']
__metaclass__ = PoolMeta


class Sale:
    __name__ = 'sale.sale'

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
