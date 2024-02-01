# Copyright 2024 Alberto Martínez <alberto.martínez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class PartnerInvoicingFrecuencyMixin(models.AbstractModel):
    _name = 'partner.invoicing.frecuency.mixin'
    _description = 'Partner Invoicing Frecuency Mixin'

    partner_invoicing_frecuency_id = fields.Many2one(
        comodel_name="partner.invoicing.frecuency",
        compute="_compute_partner_invoicing_frecuency_id",
        string="Invoicing Frecuency",
        store=True,
        readonly=False
    )

    @api.depends("partner_id")
    def _compute_partner_invoicing_frecuency_id(self):
        for rec in self:
            partner_invoicing_frecuency_id = False
            if rec.partner_id:
                partner_invoicing_frecuency_id = rec.partner_id.partner_invoicing_frecuency_id
            rec.partner_invoicing_frecuency_id = partner_invoicing_frecuency_id
