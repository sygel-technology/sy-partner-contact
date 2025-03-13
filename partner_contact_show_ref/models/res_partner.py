# Copyright 2025 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models


class Partner(models.Model):
    _inherit = "res.partner"

    def _get_complete_name(self):
        name = super()._get_complete_name()
        if self.commercial_partner_id.ref:
            name = f"[{self.commercial_partner_id.ref}] {name}"
        return name
