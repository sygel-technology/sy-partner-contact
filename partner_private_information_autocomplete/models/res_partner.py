# Copyright 2024 Roger Sans <roger.sans@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    private_phone = fields.Char(string='Private Phone',
                                store=True,
                                readonly=False,
                                compute='_compute_private_phone')

    private_mobile = fields.Char(string='Private Mobile',
                                 store=True,
                                 readonly=False,
                                 compute='_compute_private_mobile')

    private_email = fields.Char(string='Private Email',
                                store=True,
                                readonly=False,
                                compute='_compute_private_email')

    private_street = fields.Char(string='Private Street',
                                 store=True,
                                 readonly=False,
                                 compute='_compute_private_street')

    private_street2 = fields.Char(string='Private Street2',
                                  store=True,
                                  readonly=False,
                                  compute='_compute_private_street2')

    private_zip = fields.Char(string='Private Zip',
                              change_default=True,
                              store=True,
                              readonly=False,
                              compute='_compute_private_zip')

    private_city = fields.Char(string='Private City',
                               store=True,
                               readonly=False,
                               compute='_compute_private_city')

    @api.depends('phone')
    def _compute_private_phone(self):
        self.private_phone = self.phone \
            if not self.private_phone \
            else self.private_phone

    @api.depends('mobile')
    def _compute_private_mobile(self):
        self.private_mobile = self.mobile \
            if not self.private_mobile \
            else self.private_mobile

    @api.depends('email')
    def _compute_private_email(self):
        self.private_email = self.email \
            if not self.private_email \
            else self.private_email

    @api.depends('street')
    def _compute_private_street(self):
        self.private_street = self.street \
            if not self.private_street \
            else self.private_street

    @api.depends('street2')
    def _compute_private_street2(self):
        self.private_street2 = self.street2 \
            if not self.private_street2 \
            else self.private_street2

    @api.depends('zip')
    def _compute_private_zip(self):
        self.private_zip = self.zip \
            if not self.private_zip \
            else self.private_zip

    @api.depends('city')
    def _compute_private_city(self):
        self.private_city = self.city \
            if not self.private_city \
            else self.private_city

    @api.depends('category_ids')
    def _compute_private_category_ids(self):
        self.private_category_ids = self.category_ids \
            if not self.private_category_ids \
            else self.private_category_ids
