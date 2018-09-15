# This file is part pyme module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['Employee']


class Employee(metaclass=PoolMeta):
    __name__ = 'company.employee'
    active = fields.Boolean('Active', select=True)

    @staticmethod
    def default_active():
        return True
