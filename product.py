#This file is part pyme module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.

from trytond.model import ModelView, ModelSQL, fields
from trytond.tools import safe_eval, datetime_strftime
from trytond.transaction import Transaction
from trytond.pool import Pool

class Template(ModelSQL, ModelView):
    _name = 'product.template'

    def create(self, values):
        """Create product by default taxes"""
        tax_customer = u'IVA 21%'
        tax_supplier = u'21% IVA Soportado (operaciones corrientes)'

        values = values.copy()
        company = Transaction().context.get('company')

        if not values.get('customer_taxes'):
            tax = Pool().get('account.tax').search(['name','=',tax_customer], limit=1)
            if len(tax)>0:
                values['customer_taxes'] = [('set', [tax[0]])]

        if not values.get('supplier_taxes'):
            tax = Pool().get('account.tax').search(['name','=',tax_supplier], limit=1)
            if len(tax)>0:
                values['supplier_taxes'] = [('set', [tax[0]])]
        
        template_id = super(Template, self).create(values)
        return template_id

Template()
