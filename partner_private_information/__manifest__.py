# Copyright 2024 Roger Sans <roger.sans@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Partner Private Information",
    "version": "18.0.1.0.0",
    "license": "AGPL-3",
    "author": "Sygel, Odoo Community Association (OCA)",
    "category": "Contacts",
    "summary": "Add private information tab in partners.",
    "website": "https://github.com/sygel-technology/sy-partner-contact",
    "depends": [
        "contacts",
    ],
    "data": [
        "security/partner_private_information_security.xml",
        "views/res_partner_view.xml",
        "views/res_partner_category_views.xml",
    ],
}
