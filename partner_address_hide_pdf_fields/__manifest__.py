# Copyright 2024 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Partner Address Hide PDF Fields",
    "summary": "Base module to hide new partner address fields in pdf",
    "version": "18.0.1.1.0",
    "category": "Partner Management",
    "website": "https://github.com/sygel-technology/sy-partner-contact",
    "author": "Sygel",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "base",
    ],
    "data": [
        "views/res_country_views.xml",
    ],
}
