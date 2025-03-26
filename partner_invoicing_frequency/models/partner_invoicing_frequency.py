# Copyright 2024 Alberto Martínez <alberto.martínez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class PartnerInvoicingfrequency(models.Model):
    _name = "partner.invoicing.frequency"
    _description = "Invoicing frequency"

    name = fields.Char(required=True)
