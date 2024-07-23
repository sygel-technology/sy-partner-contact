# Copyright 2024 Roger Sans <roger.sans@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    private_phone = fields.Char(
        string="Internal Phone",
        groups="partner_private_information.group_partner_private_info",
    )
    private_mobile = fields.Char(
        string="Internal Mobile",
        groups="partner_private_information.group_partner_private_info",
    )
    private_email = fields.Char(
        string="Internal Email",
        groups="partner_private_information.group_partner_private_info",
    )
    private_notes = fields.Text(
        string="Internal Notes",
        groups="partner_private_information.group_partner_private_info",
    )
    private_street = fields.Char(
        string="Internal Street",
        groups="partner_private_information.group_partner_private_info",
    )
    private_street2 = fields.Char(
        string="Internal Street2",
        groups="partner_private_information.group_partner_private_info",
    )
    private_zip = fields.Char(
        string="Internal Zip",
        change_default=True,
        groups="partner_private_information.group_partner_private_info",
    )
    private_city = fields.Char(
        string="Internal City",
        groups="partner_private_information.group_partner_private_info",
    )
    private_state_id = fields.Many2one(
        "res.country.state",
        string="Internal State",
        ondelete="restrict",
        domain="[('country_id', '=?', private_country_id)]",
        groups="partner_private_information.group_partner_private_info",
    )
    private_country_id = fields.Many2one(
        "res.country",
        string="Internal Country",
        ondelete="restrict",
        groups="partner_private_information.group_partner_private_info",
    )
    private_country_code = fields.Char(
        related="country_id.code",
        string="Internal Country Code",
        groups="partner_private_information.group_partner_private_info",
    )
    private_category_ids = fields.Many2many(
        "res.partner.category",
        "private_partner_category_rel",
        string="Internal Tags",
        groups="partner_private_information.group_partner_private_info",
    )

    @api.model
    def _address_fields(self):
        res = super()._address_fields()
        res += [
            "private_street",
            "private_street2",
            "private_city",
            "private_state_id",
            "private_zip",
            "private_country_id",
        ]
        return res
