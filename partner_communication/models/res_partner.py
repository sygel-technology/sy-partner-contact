# Copyright 2023 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    partner_communication_channel_id = fields.Many2one(
        comodel_name="partner.communication.channel",
        string="Communication Channel"
    )
