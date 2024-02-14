# Copyright 2023 Ángel García de la Chica <angel.garcia@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Partner Contact Old Migration Fields",
    "summary": "Partner Contact Old Migration Fields",
    "version": "16.0.1.0.0",
    "category": "Contact",
    "website": "https://www.sygel.es",
    "author": "Sygel, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        'base',
        'contacts'
    ],   
    "data": [
        "views/res_partner_views.xml",
    ],
}
