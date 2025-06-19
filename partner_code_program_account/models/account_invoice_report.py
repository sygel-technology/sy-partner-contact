# Copyright 2024 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models
from odoo.tools import SQL


class AccountInvoiceReport(models.Model):
    _inherit = "account.invoice.report"

    code_program_id = fields.Many2one(
        string="Code Program",
        comodel_name="res.partner.code.program",
    )

    @api.model
    def _select(self) -> SQL:
        return SQL("%s, partner.code_program_id AS code_program_id", super()._select())
