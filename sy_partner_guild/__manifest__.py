# Copyright 2026 Ángel Rivas <angel.rivas@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Partner Guild",
    "version": "18.0.1.0.0",
    "category": "Partner",
    "summary": "Manage guilds on partners",
    "author": "Sygel",
    "website": "https://github.com/sygel-technology/sy-partner-contact",
    "license": "AGPL-3",
    "depends": [
        "contacts",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/res_partner_guild_views.xml",
        "views/res_partner_views.xml",
    ],
    "installable": True,
}
