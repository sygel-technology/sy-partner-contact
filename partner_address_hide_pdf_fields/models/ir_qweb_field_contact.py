# Copyright 2024 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models


class Contact(models.AbstractModel):
    _inherit = "ir.qweb.field.contact"

    def value_to_html(self, value, options):
        self.env.context = self.with_context(inside_pdf=True).env.context
        return super().value_to_html(value, options)
