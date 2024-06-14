# Copyright 2024 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class AccountInvoiceReport(models.Model):
    _inherit = "account.invoice.report"

    code_program_territory_id = fields.Many2one(
        string="Code Program Territory",
        comodel_name="res.partner.code.program.territory",
    )

    def _select(self):
        select_str = super()._select()
        return "%s, partner.code_program_territory_id" % select_str
