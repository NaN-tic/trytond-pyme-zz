#This file is part pyme module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.pool import Pool, PoolMeta

__all__ = ['Party']
__metaclass__ = PoolMeta


class Party:
    __name__ = 'party.party'

    @staticmethod
    def default_sale_price_list():
        Config = Pool().get('sale.configuration')
        config = Config(1)
        if config.sale_price_list:
            return config.sale_price_list.id
