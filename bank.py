#This file is part party_bank_validation module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.pool import Pool, PoolMeta
from trytond.transaction import Transaction

__all__ = ['BankAccount']
__metaclass__ = PoolMeta


class BankAccount:
    'Bank Account'
    __name__ = 'bank.account'

    @staticmethod
    def default_bank_country():
        return 'ES'

    @staticmethod
    def default_currency():
        Company = Pool().get('company.company')
        if Transaction().context.get('company'):
            company = Company(Transaction().context['company'])
            return company.currency.id
