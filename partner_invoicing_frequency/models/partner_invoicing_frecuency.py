# Copyright 2024 Alberto Martínez <alberto.martínez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class PartnerInvoicingFrecuency(models.Model):
    _name = "partner.invoicing.frecuency"
    _description = "Invoicing Frecuency"

    name = fields.Char(required=True)
