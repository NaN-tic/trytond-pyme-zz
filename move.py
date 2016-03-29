# This file is part pyme module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import PoolMeta
from trytond.pyson import Eval, If, Equal

__all__ = ['Move']


class Move:
    __metaclass__ = PoolMeta
    __name__ = 'stock.move'

    @classmethod
    def view_attributes(cls):
        return super(Move, cls).view_attributes() + [
            ('/tree', 'colors',
                If(Equal(Eval('state'), 'draft'), 'blue', 'black'),
                )]
