# Copyright 2024 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo.tests.common import TransactionCase


class TestPartnerChildrenAddressAutocreate(TransactionCase):
    def setUp(self):
        super().setUp()

    def test_address_autocreate(self):
        partner_id = self.env["res.partner"].create(
            {"name": "Test Partner", "is_company": True}
        )
        self.assertEqual(
            len(partner_id.child_ids),
            2,
        )

    def test_not_autocreate(self):
        partner_id = self.env["res.partner"].create(
            {"name": "Test Partner 1", "is_company": False}
        )
        self.assertEqual(
            len(partner_id.child_ids),
            0,
        )

        partner_id = (
            self.env["res.partner"]
            .with_context(**{"skip_partner_children_address_autocreate": True})
            .create({"name": "Test Partner 2", "is_company": True})
        )
        self.assertEqual(
            len(partner_id.child_ids),
            0,
        )
