# Copyright 2024 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResPartnerIdCategory(models.Model):
    _inherit = "res.partner.id_category"

    check_number = fields.Boolean(
        default=True,
        help="If unchecked, any partner identification using this type will be valid.",
    )

    def validate_id_number(self, id_number):
        self.ensure_one()
        if not self.check_number:
            return False
        else:
            return super().validate_id_number(id_number)
