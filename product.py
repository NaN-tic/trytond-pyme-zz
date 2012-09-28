#This file is part pyme module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.

from trytond.model import ModelView, ModelSQL, fields
from trytond.tools import safe_eval, datetime_strftime
from trytond.transaction import Transaction
from trytond.pool import Pool

class Template(ModelSQL, ModelView):
    _name = 'product.template'

    def default_account_category(self):
        return True

    def default_customer_taxes(self):
        config_obj = Pool().get('account.configuration')
        customer_tax = config_obj.browse(1).default_customer_tax
        return [customer_tax.id]

    def default_supplier_taxes(self):
        config_obj = Pool().get('account.configuration')
        supplier_tax = config_obj.browse(1).default_supplier_tax
        return [supplier_tax.id]

Template()
