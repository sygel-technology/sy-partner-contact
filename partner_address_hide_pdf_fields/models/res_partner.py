# Copyright 2024 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    def _display_address_inside_pdf(self):
        return self.env.context.get("inside_pdf", False)

    @api.model
    def _hided_in_pdf_address_fields(self):
        return []

    def _prepare_display_address(self, without_company=False):
        address_format, args = super()._prepare_display_address(without_company)
        if self._display_address_inside_pdf():
            args.update({key: "" for key in self._hided_in_pdf_address_fields()})
        return address_format, args
