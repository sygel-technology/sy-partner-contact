# Copyright 2026 Ángel Rivas <angel.rivas@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    guild_ids = fields.Many2many(
        comodel_name="res.partner.guild",
        string="Guilds",
    )

    def _commercial_fields(self):
        return super()._commercial_fields() + ["guild_ids"]
