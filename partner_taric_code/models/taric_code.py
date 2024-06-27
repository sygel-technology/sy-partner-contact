# Copyright 2024 Roger Sans <roger.sans@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class TaricCode(models.Model):
    _inherit = 'taric.code'
    _description = "Add TARIC code relation to partner."

    partner_ids = fields.Many2many(
        comodel_name='res.partner', 
        relation='taric_partner_rel',
        string='Partner'
        )