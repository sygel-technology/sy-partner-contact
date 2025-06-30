# Copyright 2024 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ResPartnerCodeProgramMixin(models.AbstractModel):
    _name = "res.partner.code.program.mixin"
    _description = (
        "Mixin model for applying to any object that wants to have a code program"
    )

    code_program_id = fields.Many2one(
        string="Code Program",
        comodel_name="res.partner.code.program",
        compute="_compute_code_program_id",
        store=True,
        readonly=False,
    )

    @api.depends("partner_id")
    def _compute_code_program_id(self):
        for rec in self:
            rec.code_program_id = rec.partner_id.code_program_id
