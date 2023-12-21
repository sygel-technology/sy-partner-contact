# Copyright 2023 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class PartnerCommunicationChannelMixin(models.AbstractModel):
    _name = 'partner.communication.channel.mixin'
    _description = 'Partner Communication Channel Mixin'

    partner_communication_channel_id = fields.Many2one(
        comodel_name="partner.communication.channel",
        compute="_compute_partner_communication_channel_id",
        string="Communication Channel",
        store=True,
        readonly=False
    )

    @api.depends("partner_id")
    def _compute_partner_communication_channel_id(self):
        for sel in self:
            partner_communication_channel_id = False
            if sel.partner_id:
                partner_communication_channel_id = sel.partner_id.partner_communication_channel_id
            sel.partner_communication_channel_id = partner_communication_channel_id
