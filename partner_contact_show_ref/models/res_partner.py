# Copyright 2025 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class Partner(models.Model):
    _inherit = "res.partner"

    own_ref_in_name = fields.Boolean()

    def _get_complete_name(self):
        name = super()._get_complete_name()
        ref = self.ref if self.own_ref_in_name else self.commercial_partner_id.ref
        if ref:
            name = f"[{ref}] {name}"
        return name
