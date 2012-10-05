#This file is part pyme module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.
{
    'name': 'PyME',
    'name_ca_ES': 'PyME',
    'name_es_ES': 'PyME',
    'version': '2.4.0',
    'author': 'Zikzakmedia',
    'email': 'zikzak@zikzakmedia.com',
    'website': 'http://www.zikzakmedia.com/',
    'description': '''PyME. Spanish localization''',
    'description_ca_ES': '''PyME. Localització espanyola''',
    'description_es_ES': '''PyME. Localización española''',
    'depends': [
        'account_code_digits',
        'account_es',
        'account_invoice_cancel',
        'country_zip_es',
        'party_bank_es',
    ],
    'xml': [
        'account.xml',
    ],
    'translation': [
        'locale/ca_ES.po',
        'locale/es_ES.po',
    ]
}
