# This file is part pyme module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import PoolMeta, Pool
from trytond.model import fields
from trytond.pyson import Eval, If, Equal

__all__ = ['Invoice']


class Invoice(metaclass=PoolMeta):
    __name__ = 'account.invoice'
    email = fields.Function(fields.Char('E-mail'), 'get_email')

    def get_email(self, name):
        return self.party.email if self.party else None

    # @classmethod
    # def view_attributes(cls):
    #     return super(Invoice, cls).view_attributes() + [
    #         ('/tree', 'colors',
    #             If(Equal(Eval('state'), 'draft'), 'blue',
    #             If(Equal(Eval('state'), 'validated'), 'green',
    #             If(Equal(Eval('state'), 'posted'), 'brown',
    #             If(Equal(Eval('state'), 'cancel'), 'grey', 'black')))),
    #             )]

    def get_move(self):
        move = super(Invoice, self).get_move()
        if self.description:
            move.description = self.description
        return move

    def _get_move_line(self, date, amount):
        Config = Pool().get('account.configuration')

        config = Config(1)
        line = super(Invoice, self)._get_move_line(date, amount)

        description = ''
        for field in config.description_for_account_move_line.split('+'):
            if description:
                description += ' - '
            description += getattr(self, field, '') or ''
        line.description = description
        return line
