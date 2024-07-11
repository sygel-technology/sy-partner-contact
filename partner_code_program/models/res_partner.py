# Copyright 2024 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    code_program_id = fields.Many2one(
        string="Code Program",
        comodel_name="res.partner.code.program",
        ondelete="restrict",
    )
    code_program_name = fields.Char(
        string="Code Program Name",
        related="code_program_id.name",
    )

    @api.model
    def _address_fields(self):
        return super()._address_fields() + ["code_program_id", "code_program_name"]

    @api.model
    def _commercial_fields(self):
        return super()._commercial_fields() + ["code_program_id"]
