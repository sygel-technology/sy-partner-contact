# Copyright 2024 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ResCityZip(models.Model):
    _inherit = "res.city.zip"

    _rec_names_search = [
        "name",
        "city_id",
        "state_id",
        "country_id",
        "code_program_id",
        "code_program_territory_id",
    ]

    code_program_id = fields.Many2one(
        string="Code Program",
        comodel_name="res.partner.code.program",
    )

    code_program_territory_id = fields.Many2one(
        string="Code Program Territory",
        comodel_name="res.partner.code.program.territory",
        domain="['|', ('code_program_id', '=?', code_program_id),\
            ('code_program_id', '=', False)]",
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

    @api.depends(
        "code_program_id",
        "code_program_id.name",
        "code_program_territory_id",
        "code_program_territory_id.name",
    )
    def _compute_display_name(self):
        res = super()._compute_display_name()
        for rec in self:
            name_add = ""
            if rec.code_program_territory_id:
                name_add += f"{rec.code_program_territory_id.name}, "
            if rec.code_program_id:
                name_add += f"{rec.code_program_id.name}, "
            if name_add:
                rec.display_name = rec.display_name.replace(
                    rec.country_id.name, name_add + rec.country_id.name
                )
        return res
