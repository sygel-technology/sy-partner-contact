# Copyright 2024 Alberto Martínez <alberto.martínez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Partner Invoicing Frecuency",
    "summary": "Select a invoicing frecuency in partners",
    "version": "16.0.1.0.0",
    "license": "AGPL-3",
    "author": "Sygel",
    "category": "Contact",
    "depends": [
        "contacts",
        "sale",
        "account",
        "purchase",
        "stock"
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/partner_invoicing_frecuency_views.xml",
        "views/res_partner_views.xml",
        "views/sale_order_views.xml",
        "views/account_move_views.xml",
        "views/purchase_views.xml",
        "views/stock_picking_views.xml"
    ],
    "installable": True,
}
