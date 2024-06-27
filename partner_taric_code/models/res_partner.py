# Copyright 2024 Roger Sans <roger.sans@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class ResPartner(models.Model):
    _inherit = 'res.partner'
    _description = "Add TARIC codes to partner."

    taric_code_ids = fields.Many2many(
        comodel_name='taric.code', 
        relation='taric_partner_rel',
        string='TARIC'
        )
    