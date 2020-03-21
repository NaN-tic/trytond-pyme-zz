# This file is part of totenart module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import PoolMeta
from trytond.transaction import Transaction
from trytond.i18n import gettext
from trytond.exceptions import UserError

__all__ = ['Module']


class Module(metaclass=PoolMeta):
    __name__ = "ir.module"

    @classmethod
    def activate(cls, modules):
        if Transaction().user != 0:
            raise UserError(gettext('pyme.msg_activation_error'))
        super(Module, cls).activate(modules)

    @classmethod
    def deactivate(cls, modules):
        if Transaction().user != 0:
            raise UserError(gettext('pyme.msg_activation_error'))
        super(Module, cls).deactivate(modules)
