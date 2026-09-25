# Copyright 2026 Ángel Rivas <angel.rivas@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, fields, models


class ResPartnerGuild(models.Model):
    _name = "res.partner.guild"
    _description = "Partner Guild"
    _order = "name"

    name = fields.Char(
        required=True,
        translate=True,
    )
    active = fields.Boolean(
        default=True,
    )
    color = fields.Integer(
        default=0,
    )

    _sql_constraints = [
        (
            "name_uniq",
            "unique(name)",
            "The guild name must be unique.",
        ),
    ]

    def copy(self, default=None):
        self.ensure_one()
        default = dict(default or {})
        default.setdefault("name", _("%s (copy)", self.name))
        return super().copy(default)
