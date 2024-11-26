# Copyright 2024 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Partner Identification Disable",
    "summary": "Do not check identification numbers",
    "version": "16.0.1.0.0",
    "category": "Contact",
    "website": "https://github.com/sygel-technology/sy-partner-contact",
    "author": "Sygel, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "partner_identification",
    ],
    "data": ["views/res_partner_id_category_view.xml"],
}
