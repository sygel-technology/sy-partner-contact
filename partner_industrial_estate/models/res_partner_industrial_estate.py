# Copyright 2024 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, fields, models


class ResPartnerIndustrialEstate(models.Model):
    _name = "res.partner.industrial.estate"
    _description = "Industrial Estate"

    _rec_names_search = ["name", "code"]

    name = fields.Char(required=True, translate=True)
    code = fields.Char(
        required=True,
    )
    res_partner_count = fields.Integer(
        compute="_compute_res_partner_count", string="Number of Contacts"
    )

    def _compute_res_partner_count(self):
        for rec in self:
            rec.res_partner_count = self.env["res.partner"].search_count(
                [("industrial_estate_id", "=", rec.id)]
            )

    def action_view_res_partner(self):
        return {
            "type": "ir.actions.act_window",
            "res_model": "res.partner",
            "name": _("Contacts"),
            "views": [(False, "list"), (False, "form")],
            "domain": [("industrial_estate_id", "=", self.id)],
        }

    _sql_constraints = [
        (
            "name_uniq",
            "UNIQUE(name)",
            "You already have a industrial state with that name. "
            "The name must be unique. ",
        ),
        (
            "code_uniq",
            "UNIQUE(code)",
            "You already have a industrial state with that code. "
            "The code must be unique. ",
        ),
    ]
