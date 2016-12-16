# This file is part pyme module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
from trytond.pool import Pool
import account
import attachment
import bank
import company
import invoice
import product
import purchase
import sale
import stock

def register():
    Pool.register(
        account.AccountConfiguration,
        account.TaxLine,
        attachment.Attachment,
        bank.BankAccount,
        company.Employee,
        invoice.Invoice,
        invoice.InvoiceLine,
        product.ProductTemplate,
        purchase.Purchase,
        sale.Sale,
        stock.Move,
        stock.ShipmentIn,
        stock.ShipmentInReturn,
        stock.ShipmentInternal,
        stock.ShipmentOut,
        stock.ShipmentOutReturn,
        module='pyme', type_='model')
