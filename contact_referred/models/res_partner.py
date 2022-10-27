# Copyright 2022 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields


class ResPartner(models.Model):
    _inherit = "res.partner"

    referred_contact_id = fields.Many2one(
        string="Referred Contact",
        comodel_name="res.partner"
    )
