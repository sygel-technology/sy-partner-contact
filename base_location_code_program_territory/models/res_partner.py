# Copyright 2024 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    code_program_id = fields.Many2one(
        compute="_compute_code_program_id",
        store=True,
        readonly=False,
    )
    code_program_territory_id = fields.Many2one(
        compute="_compute_code_program_territory_id",
        store=True,
        readonly=False,
    )

    @api.depends("code_program_id", "code_program_territory_id")
    def _compute_zip_id(self):
        res = super()._compute_zip_id()
        for record in self.filtered("zip_id"):
            fields = ["code_program_id", "code_program_territory_id"]
            for field in fields:
                if (
                    record[field]
                    and record[field] != record._origin[field]
                    and record[field] != record.zip_id[field]
                ):
                    record.zip_id = False
                    break
        return res

    @api.depends("zip_id")
    def _compute_code_program_id(self):
        for record in self:
            if record.zip_id:
                record.code_program_id = record.zip_id.code_program_id

    @api.depends("zip_id")
    def _compute_code_program_territory_id(self):
        for record in self:
            if record.zip_id:
                record.code_program_territory_id = (
                    record.zip_id.code_program_territory_id
                )
