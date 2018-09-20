# This file is part pyme module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
from . import account
from . import attachment
from . import bank
from . import company
from . import invoice
from . import product
from . import purchase
from . import sale
from . import stock

def register():
    Pool.register(
        account.AccountConfiguration,
        account.TaxLine,
        attachment.Attachment,
        bank.BankAccount,
        company.Employee,
        invoice.Invoice,
        invoice.InvoiceLine,
        product.ProductCategory,
        product.ProductTemplate,
        purchase.Purchase,
        purchase.PurchaseLine,
        sale.Sale,
        sale.SaleLine,
        stock.Move,
        stock.ShipmentIn,
        stock.ShipmentInReturn,
        stock.ShipmentInternal,
        stock.ShipmentOut,
        stock.ShipmentOutReturn,
        module='pyme', type_='model')
