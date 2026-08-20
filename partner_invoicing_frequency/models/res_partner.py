# Copyright 2024 Alberto Martínez <alberto.martínez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    partner_invoicing_frequency_id = fields.Many2one(
        comodel_name="partner.invoicing.frequency", string="Invoicing frequency"
    )

    @api.model
    def _commercial_fields(self):
        return super()._commercial_fields() + ["partner_invoicing_frequency_id"]
