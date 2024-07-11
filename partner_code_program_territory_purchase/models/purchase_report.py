# Copyright 2024 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class PurchaseReport(models.Model):
    _inherit = "purchase.report"

    code_program_territory_id = fields.Many2one(
        string="Code Program Territory",
        comodel_name="res.partner.code.program.territory",
    )

    def _select(self):
        return (
            super(PurchaseReport, self)._select()
            + ", partner.code_program_territory_id as code_program_territory_id"
        )

    def _group_by(self):
        return (
            super(PurchaseReport, self)._group_by()
            + ", partner.code_program_territory_id"
        )
