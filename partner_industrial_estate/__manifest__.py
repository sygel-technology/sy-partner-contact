# Copyright 2024 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Partner Industrial Estate",
    "summary": "Adds the partner industrial estate fields on contacts",
    "version": "18.0.1.0.0",
    "category": "Partner Management",
    "website": "https://github.com/sygel-technology/sy-partner-contact",
    "author": "Sygel",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "contacts",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/res_partner_industrial_estate_views.xml",
        "views/res_partner_views.xml",
    ],
    "post_init_hook": "post_init_hook",
    "uninstall_hook": "uninstall_hook",
}
