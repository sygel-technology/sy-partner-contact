# Copyright 2022 Ángel García de la Chica Herrera <angel.garcia@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields


class Partner(models.Model):
    _inherit = "res.partner"

    old_customer_acc_number = fields.Char(
        string='Old customer account number',
    )
    old_vendor_acc_number = fields.Char(
        string='Old vendor account number',
    )
