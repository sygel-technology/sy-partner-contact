# Copyright 2024 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Partner Code Program Territory Account",
    "summary": "Adds the partner code program territory fields on accounting",
    "version": "18.0.1.0.0",
    "category": "Partner Management",
    "website": "https://github.com/sygel-technology/sy-partner-contact",
    "author": "Sygel",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": ["partner_code_program_territory", "account"],
    "data": [
        "views/account_invoice_report.xml",
        "views/account_move.xml",
    ],
}
