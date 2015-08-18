# This file is part pyme module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import PoolMeta
from trytond.pyson import Eval, If, Equal

__all__ = ['ShipmentIn', 'ShipmentInReturn', 'ShipmentInternal',
        'ShipmentOut', 'ShipmentOutReturn']
__metaclass__ = PoolMeta


class ShipmentIn:
    __name__ = 'stock.shipment.in'

    @classmethod
    def view_attributes(cls):
        return [('/tree', 'colors',
                If(Equal(Eval('state'), 'draft'), 'blue',
                If(Equal(Eval('state'), 'received'), 'darkgreen',
                If(Equal(Eval('state'), 'cancel'), 'grey', 'black'))),
                )]


class ShipmentInReturn:
    __name__ = 'stock.shipment.in.return'

    @classmethod
    def view_attributes(cls):
        return [('/tree', 'colors',
                If(Equal(Eval('state'), 'draft'), 'blue',
                If(Equal(Eval('state'), 'waiting'), 'brown',
                If(Equal(Eval('state'), 'assigned'), 'darkgreen',
                If(Equal(Eval('state'), 'cancel'), 'grey', 'black')))),
                )]


class ShipmentInternal:
    __name__ = 'stock.shipment.internal'

    @classmethod
    def view_attributes(cls):
        return [('/tree', 'colors',
                If(Equal(Eval('state'), 'draft'), 'blue',
                If(Equal(Eval('state'), 'waiting'), 'brown',
                If(Equal(Eval('state'), 'assigned'), 'darkgreen',
                If(Equal(Eval('state'), 'cancel'), 'grey', 'black')))),
                )]


class ShipmentOut:
    __name__ = 'stock.shipment.out'

    @classmethod
    def view_attributes(cls):
        return [('/tree', 'colors',
                If(Equal(Eval('state'), 'draft'), 'blue',
                If(Equal(Eval('state'), 'waiting'), 'brown',
                If(Equal(Eval('state'), 'assigned'), 'darkgreen',
                If(Equal(Eval('state'), 'cancel'), 'grey', 'black')))),
                )]


class ShipmentOutReturn:
    __name__ = 'stock.shipment.out.return'

    @classmethod
    def view_attributes(cls):
        return [('/tree', 'colors',
                If(Equal(Eval('state'), 'draft'), 'blue',
                If(Equal(Eval('state'), 'received'), 'darkgreen',
                If(Equal(Eval('state'), 'cancel'), 'grey', 'black'))),
                )]
