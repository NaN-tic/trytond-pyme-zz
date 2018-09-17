# This file is part of totenart module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import PoolMeta
from trytond.transaction import Transaction

__all__ = ['Module']


class Module(metaclass=PoolMeta):
    __name__ = "ir.module"

    @classmethod
    def __setup__(cls):
        super(Module, cls).__setup__()
        cls._error_messages.update({
                'activation_error': 'You cannot modify the state of a module '
                    'since desktop client because this is a balanced server.\n'
                    'Please, contact with your TIC provider in order to do it '
                    'for you. Thank you.',
                })

    @classmethod
    def activate(cls, modules):
        if Transaction().user != 0:
            cls.raise_user_error('activation_error')
        super(Module, cls).activate(modules)

    @classmethod
    def deactivate(cls, modules):
        if Transaction().user != 0:
            cls.raise_user_error('activation_error')
        super(Module, cls).deactivate(modules)
