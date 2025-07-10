# Copyright 2024 Roger Sans <roger.sans@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
import re

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


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

    @api.constrains("private_phone", "private_mobile", "private_email")
    def _check_internal_contact_info_format(self):
        phone_pattern = re.compile(r"^\+?[0-9\s\-]{7,20}$")
        email_pattern = re.compile(r"^[\w\.-]+@[\w\.-]+\.\w+$")

        for record in self:
            if record.private_phone and not phone_pattern.match(record.private_phone):
                raise ValidationError(
                    _(
                        "Invalid format for Private Phone. Examples: "
                        "'+34 912 345 678', '912-345-678'."
                    )
                )
            if record.private_mobile and not phone_pattern.match(record.private_mobile):
                raise ValidationError(
                    _(
                        "Invalid format for Private Mobile. Examples: "
                        "'+34 600 100 200', '601-602-603'."
                    )
                )
            if record.private_email and not email_pattern.match(record.private_email):
                raise ValidationError(
                    _(
                        "Invalid format for Private Email."
                        "Example: 'john.doe@example.com'."
                    )
                )

    @api.onchange("private_phone", "country_id", "company_id")
    def _onchange_private_phone_validation(self):
        if self.private_phone:
            self.private_phone = (
                self._phone_format(fname="private_phone", force_format="INTERNATIONAL")
                or self.private_phone
            )

    @api.onchange("private_mobile", "country_id", "company_id")
    def _onchange_private_mobile_validation(self):
        if self.private_mobile:
            self.private_mobile = (
                self._phone_format(fname="private_mobile", force_format="INTERNATIONAL")
                or self.private_mobile
            )
