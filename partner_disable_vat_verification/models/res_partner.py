# Copyright 2024 Ángel García de la Chica Herrera <angel.garcia@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.constrains("vat", "country_id")
    def check_vat(self):
        return super(ResPartner, self.with_context(no_vat_validation=True)).check_vat()
