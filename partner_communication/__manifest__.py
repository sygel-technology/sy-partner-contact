# Copyright 2023 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    "name": "Partner Communication",
    "summary": "Select a communication channel in partners",
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
        "views/partner_communication_channel_views.xml",
        "views/res_partner_views.xml",
        "views/sale_order_views.xml",
        "views/account_move_views.xml",
        "views/purchase_views.xml",
        "views/stock_picking_views.xml"
    ],
    "installable": True,
}
