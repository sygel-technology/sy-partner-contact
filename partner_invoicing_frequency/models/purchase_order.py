# Copyright 2024 Alberto Martínez <alberto.martínez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models


class PurchaseOrder(models.Model):
    _name = "purchase.order"
    _inherit = ["purchase.order", "partner.invoicing.frequency.mixin"]
