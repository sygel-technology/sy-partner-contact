# Copyright 2024 Alberto Martínez <alberto.martínez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class PartnerInvoicingfrequencyMixin(models.AbstractModel):
    _name = "partner.invoicing.frequency.mixin"
    _description = "Partner Invoicing frequency Mixin"

    partner_invoicing_frequency_id = fields.Many2one(
        comodel_name="partner.invoicing.frequency",
        compute="_compute_partner_invoicing_frequency_id",
        string="Invoicing frequency",
        store=True,
        readonly=False,
    )

    @api.depends("partner_id")
    def _compute_partner_invoicing_frequency_id(self):
        for rec in self:
            partner_invoicing_frequency_id = False
            if rec.partner_id:
                partner_invoicing_frequency_id = (
                    rec.partner_id.partner_invoicing_frequency_id
                )
            rec.partner_invoicing_frequency_id = partner_invoicing_frequency_id
