# Copyright 2024 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    industrial_estate_id = fields.Many2one(
        string="Industrial Estate",
        comodel_name="res.partner.industrial.estate",
        ondelete="restrict",
    )
    industrial_estate_name = fields.Char(
        string="Industrial Estate Name",
        related="industrial_estate_id.name",
    )

    @api.model
    def _address_fields(self):
        return super()._address_fields() + [
            "industrial_estate_id",
            "industrial_estate_name",
        ]

    @api.model
    def _commercial_fields(self):
        return super()._commercial_fields() + ["industrial_estate_id"]
