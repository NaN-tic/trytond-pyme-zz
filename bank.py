#This file is part party_bank_validation module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.
from trytond.pool import PoolMeta

__all__ = ['BankAccount']
__metaclass__ = PoolMeta

class BankAccount:
    'Bank Account'
    __name__ = 'bank.account'

    @staticmethod
    def default_bank_country():
        return 'ES'
