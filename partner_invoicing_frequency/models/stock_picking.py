# Copyright 2024 Alberto Martínez <alberto.martínez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models


class StockPicking(models.Model):
    _name = "stock.picking"
    _inherit = ["stock.picking", "partner.invoicing.frequency.mixin"]
