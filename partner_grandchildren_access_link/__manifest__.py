# Copyright 2024 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Partner Grandchildren Access Link",
    "summary": "Notebook tag with computed partner grandchildrens in contacts",
    "version": "17.0.1.0.0",
    "category": "Contacts",
    "website": "https://github.com/sygel-technology/sy-partner-contact",
    "author": "Sygel, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "partner_grandchildren",
        "partner_contact_access_link",
    ],
    "data": [
        "views/res_partner.xml",
    ],
}
