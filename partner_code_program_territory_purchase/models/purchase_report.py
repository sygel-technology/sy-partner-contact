# Copyright 2024 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models
from odoo.tools import SQL


class PurchaseReport(models.Model):
    _inherit = "purchase.report"

    code_program_territory_id = fields.Many2one(
        string="Code Program Territory",
        comodel_name="res.partner.code.program.territory",
    )

    def _select(self):
        return SQL(
            "%s, partner.code_program_territory_id as code_program_territory_id",
            super()._select(),
        )

    def _group_by(self):
        return SQL("%s, partner.code_program_territory_id", super()._group_by())
