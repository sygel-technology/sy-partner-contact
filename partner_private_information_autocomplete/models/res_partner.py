# Copyright 2024 Roger Sans <roger.sans@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    private_zip_id = fields.Many2one(
        comodel_name="res.city.zip",
        string="Internal ZIP Location",
        index=True,
        compute="_compute_private_zip_id",
        readonly=False,
        store=True,
    )
    private_zip = fields.Char(
        change_default=True,
        store=True,
        readonly=False,
        compute="_compute_private_zip",
    )
    private_city = fields.Char(
        store=True,
        readonly=False,
        compute="_compute_private_city",
    )
    private_city_id = fields.Many2one(
        "res.city",
        string="Internal City",
        ondelete="restrict",
        groups="partner_private_information.group_partner_private_info",
        store=True,
        readonly=False,
        compute="_compute_private_city_id",
    )
    private_state_id = fields.Many2one(
        store=True,
        readonly=False,
        compute="_compute_private_state_id",
    )
    private_country_id = fields.Many2one(
        store=True,
        readonly=False,
        compute="_compute_private_country_id",
    )

    @api.depends(
        "private_state_id", "private_country_id", "private_city_id", "private_zip"
    )
    def _compute_private_zip_id(self):
        """Empty the zip auto-completion field if data mismatch when on UI."""
        for record in self.filtered("private_zip_id"):
            fields_map = {
                "private_zip": "name",
                "private_city_id": "city_id",
                "private_state_id": "state_id",
                "private_country_id": "country_id",
            }
            for rec_field, zip_field in fields_map.items():
                if (
                    record[rec_field]
                    and record[rec_field] != record._origin[rec_field]
                    and record[rec_field] != record.private_zip_id[zip_field]
                ):
                    record.private_zip_id = False
                    break

    @api.depends("private_zip_id")
    def _compute_private_city_id(self):
        for record in self:
            if record.private_zip_id:
                record.private_city_id = record.private_zip_id.city_id
            elif not record.country_enforce_cities:
                record.private_city_id = False

    @api.depends("private_zip_id")
    def _compute_private_city(self):
        for record in self.filtered("private_zip_id"):
            record.private_city = record.private_zip_id.city_id.name

    @api.depends("private_zip_id")
    def _compute_private_zip(self):
        for record in self.filtered("private_zip_id"):
            record.private_zip = record.private_zip_id.name

    @api.depends("private_zip_id", "private_state_id")
    def _compute_private_country_id(self):
        for record in self:
            if record.private_zip_id.city_id.country_id:
                record.private_country_id = record.private_zip_id.city_id.country_id
            elif record.private_state_id:
                record.private_country_id = record.private_state_id.country_id

    @api.depends("private_zip_id")
    def _compute_private_state_id(self):
        for record in self:
            state = record.private_zip_id.city_id.state_id
            if state and record.private_state_id != state:
                record.private_state_id = record.private_zip_id.city_id.state_id

    @api.model
    def _address_fields(self):
        """Add to the list of address fields the new ZIP one, but also the city that is
        not added by `base_address_extended`.
        """
        return super()._address_fields() + ["private_zip_id", "private_city_id"]
