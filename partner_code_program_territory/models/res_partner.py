# Copyright 2024 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    code_program_territory_id = fields.Many2one(
        string="Code Program Territory",
        comodel_name="res.partner.code.program.territory",
        ondelete="restrict",
        domain="['|', ('code_program_id', '=?', code_program_id), ('code_program_id', '=', False)]",
    )
    code_program_territory_name = fields.Char(
        string="Code Program Territory Name",
        related="code_program_territory_id.name",
    )

    @api.onchange("code_program_id")
    def _onchange_code_program_id(self):
        if (
            self.code_program_id
            and self.code_program_id != self.code_program_territory_id.code_program_id
            and self.code_program_territory_id.code_program_id
        ):
            self.code_program_territory_id = False

    @api.onchange("code_program_territory_id")
    def _onchange_code_program_territory_id(self):
        if (
            self.code_program_territory_id.code_program_id
            and self.code_program_id != self.code_program_territory_id.code_program_id
        ):
            self.code_program_id = self.code_program_territory_id.code_program_id

    @api.model
    def _address_fields(self):
        return super()._address_fields() + [
            "code_program_territory_id",
            "code_program_territory_name",
        ]

    @api.model
    def _commercial_fields(self):
        return super()._commercial_fields() + ["code_program_territory_id"]
