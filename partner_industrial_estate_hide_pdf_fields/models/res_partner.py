# Copyright 2024 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.model
    def _hided_in_pdf_address_fields(self):
        return super()._hided_in_pdf_address_fields() + [
            "industrial_estate_id",
            "industrial_estate_name",
        ]
