# Copyright 2024 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class SaleReport(models.Model):
    _inherit = "sale.report"

    code_program_id = fields.Many2one(
        string="Code Program",
        comodel_name="res.partner.code.program",
    )

    def _select_additional_fields(self):
        res = super()._select_additional_fields()
        res["code_program_id"] = "partner.code_program_id"
        return res

    def _group_by_sale(self):
        res = super()._group_by_sale()
        res += """,
            partner.code_program_id"""
        return res
