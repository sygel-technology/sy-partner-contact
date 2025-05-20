# Copyright 2024 Alberto Martínez <alberto.martínez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Partner Invoicing Frequency",
    "summary": "Select a invoicing frequency in partners",
    "version": "17.0.1.0.2",
    "license": "AGPL-3",
    "author": "Sygel",
    "category": "Contact",
    "website": "https://github.com/sygel-technology/sy-partner-contact",
    "depends": ["contacts", "sale", "account", "purchase", "stock"],
    "data": [
        "security/ir.model.access.csv",
        "views/partner_invoicing_frequency_views.xml",
        "views/res_partner_views.xml",
        "views/sale_order_views.xml",
        "views/account_move_views.xml",
        "views/purchase_views.xml",
        "views/stock_picking_views.xml",
    ],
    "installable": True,
}
