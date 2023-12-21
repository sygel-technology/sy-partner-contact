# Copyright 2023 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models


class AccountMove(models.Model):
    _name = 'account.move'
    _inherit = ['account.move', 'partner.communication.channel.mixin']
