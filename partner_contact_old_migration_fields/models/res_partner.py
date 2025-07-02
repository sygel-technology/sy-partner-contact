# Copyright 2023 Ángel García de la Chica Herrera <angel.garcia@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class Partner(models.Model):
    _inherit = "res.partner"

    old_partner_id = fields.Integer(
        string="Old Partner ID",
    )
    old_partner_parent_id = fields.Integer(
        string="Old Partner Parent ID",
    )
