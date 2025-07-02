# Copyright 2024 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Base Location Code Program Territory",
    "summary": "Associate ZIPs to code programs and code territories",
    "version": "18.0.1.0.0",
    "category": "Partner Management",
    "website": "https://github.com/sygel-technology/sy-partner-contact",
    "author": "Sygel",
    "license": "AGPL-3",
    "application": False,
    "installable": True,
    "depends": [
        "base_location",
        "partner_code_program",
        "partner_code_program_territory",
    ],
    "data": [
        "views/res_city_zip_views.xml",
    ],
}
