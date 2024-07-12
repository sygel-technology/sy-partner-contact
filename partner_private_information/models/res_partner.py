# Copyright 2024 Roger Sans <roger.sans@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'

    private_phone = fields.Char(string='Private Phone')
    private_mobile = fields.Char(string='Private Mobile')
    private_email = fields.Char(string='Private Email')
    private_notes = fields.Text(string='Private Notes')
    private_street = fields.Char(string='Private Street')
    private_street2 = fields.Char(string='Private Street2')
    private_zip = fields.Char(string='Private Zip', change_default=True)
    private_city = fields.Char(string='Private City')
    private_state_id = fields.Many2one("res.country.state",
                                       string='Private State',
                                       ondelete='restrict',
                                       domain="[('country_id', '=?', country_id)]")
    private_country_id = fields.Many2one('res.country',
                                         string='Private Country',
                                         ondelete='restrict')
    private_country_code = fields.Char(related='country_id.code',
                                       string="Private Country Code")
    private_category_ids = fields.Many2many('res.partner.category',
                                            'private_partner_category_rel',
                                            string='Private Tags')
