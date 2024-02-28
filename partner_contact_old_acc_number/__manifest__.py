# Copyright 2022 Ángel García de la Chica <angel.garcia@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Partner contact old acc number",
    "summary": "Partner contact old acc number",
    "version": "12.0.1.0.1",
    "category": "Accounting/CRM",
    "website": "https://www.sygel.es",
    "author": "Sygel, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        'base',
        'account',
    ],   
    "data": [
        "views/res_partner_views.xml",
    ],
}
