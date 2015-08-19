# This file is part pyme module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import PoolMeta
from trytond.pyson import Eval, If, Equal

__all__ = ['Invoice']
__metaclass__ = PoolMeta


class Invoice:
    __name__ = 'account.invoice'

    @classmethod
    def view_attributes(cls):
        return super(Invoice, cls).view_attributes() + [
            ('/tree', 'colors',
                If(Equal(Eval('state'), 'draft'), 'blue', 
                If(Equal(Eval('state'), 'validated'), 'green', 
                If(Equal(Eval('state'), 'posted'), 'brown', 
                If(Equal(Eval('state'), 'cancel'), 'grey', 'black')))),
                )]
