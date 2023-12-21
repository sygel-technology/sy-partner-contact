# Copyright 2023 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class PartnercCommunicationChannel(models.Model):
    _name = "partner.communication.channel"
    _description = "Partner Communication"

    name = fields.Char(required=True)
