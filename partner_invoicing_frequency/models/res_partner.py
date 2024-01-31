# Copyright 2024 Alberto Martínez <alberto.martínez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    partner_invoicing_frecuency_id = fields.Many2one(
        comodel_name="partner.invoicing.frecuency",
        string="Invoicing Frecuency"
    )