# Copyright 2024 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, fields, models


class ResPartnerCodeProgram(models.Model):
    _inherit = "res.partner.code.program"

    code_program_territory_ids = fields.One2many(
        string="Code Program Territory",
        comodel_name="res.partner.code.program.territory",
        inverse_name="code_program_id",
    )

    code_terriroty_count = fields.Integer(
        string="Number of Code Territories",
        compute="_compute_code_terriroty_count",
    )

    def _compute_code_terriroty_count(self):
        for rec in self:
            rec.code_terriroty_count = self.env[
                "res.partner.code.program.territory"
            ].search_count([("code_program_id", "=", rec.id)])

    def action_view_code_terriroty(self):
        return {
            "type": "ir.actions.act_window",
            "res_model": "res.partner.code.program.territory",
            "name": _("Code Program Territory"),
            "views": [(False, "tree"), (False, "form")],
            "domain": [("code_program_id", "=", self.id)],
        }
