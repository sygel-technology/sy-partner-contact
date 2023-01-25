# Copyright 2023 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields


class Partner(models.Model):
    _inherit = "res.partner"

    vat = fields.Char(
        required=True
    )
