# This file is part pyme module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import PoolMeta

__all__ = ['ImportStart']


class ImportStart(metaclass=PoolMeta):
    __name__ = 'account.bank.statement.import.start'

    @staticmethod
    def default_type():
        return 'csb43'
