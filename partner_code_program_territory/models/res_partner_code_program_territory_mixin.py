# Copyright 2024 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ResPartnerCodeProgramTerritoryMixin(models.AbstractModel):
    _name = "res.partner.code.program.territory.mixin"
    _description = "Mixin model for applying to any object that wants to have a code program territory"

    code_program_territory_id = fields.Many2one(
        string="Code Program Territory",
        comodel_name="res.partner.code.program.territory",
        compute="_compute_code_program_territory_id",
        store=True,
        readonly=False,
    )

    @api.depends("partner_id")
    def _compute_code_program_territory_id(self):
        for rec in self:
            rec.code_program_territory_id = rec.partner_id.code_program_territory_id
