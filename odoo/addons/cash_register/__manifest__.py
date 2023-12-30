# Copyright (C) 2017-2021 Creu Blanca
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

{
    "name": "CASH REGISTER",
    "version": "16.0.0",
    "category": "Accounting",
    "author": "Geraldine MABA",
    "website": "https://github.com/OCA/account-payment",
    "summary": "Initiate expense and receipt documents for payments at the cash. Create bank statements",
    "license": "LGPL-3",
    'images': [
        'cash_register/static/description/icon.png',
    ],
    "depends": ['base','mail', 'contacts', 'hr'],
    "data": [
        "security/ir.model.access.csv",
        "data/cash_register_sequence.xml",
        "views/menus.xml",
        "views/account_cash_register.xml",
        "report/report_format.xml",
        "report/report_cash_register.xml",
    ],
}
