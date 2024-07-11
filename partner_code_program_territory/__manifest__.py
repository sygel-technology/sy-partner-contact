# Copyright 2024 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Partner Code Program Territory",
    "summary": "Adds the partner code program territory fields on contacts",
    "version": "17.0.1.0.0",
    "category": "Partner Management",
    "website": "https://github.com/sygel-technology/sy-partner-contact",
    "author": "Sygel",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "partner_code_program",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/res_partner_code_program_territory_views.xml",
        "views/res_partner_code_program_views.xml",
        "views/res_partner_views.xml",
    ],
    "post_init_hook": "post_init_hook",
    "uninstall_hook": "uninstall_hook",
}
