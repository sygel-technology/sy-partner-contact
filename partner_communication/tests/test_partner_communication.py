# Copyright 2026 Ángel Rivas <angel.rivas@sygel.es>
# License AGPL-3 - See https://www.gnu.org/licenses/agpl-3.0
from odoo.tests.common import TransactionCase


class TestPartnerCommunication(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.channel_email = cls.env["partner.communication.channel"].create(
            {
                "name": "Email",
            }
        )
        cls.channel_phone = cls.env["partner.communication.channel"].create(
            {
                "name": "Phone",
            }
        )

        cls.partner_1 = cls.env["res.partner"].create(
            {
                "name": "Partner 1",
                "partner_communication_channel_id": cls.channel_email.id,
            }
        )
        cls.partner_2 = cls.env["res.partner"].create(
            {
                "name": "Partner 2",
                "partner_communication_channel_id": cls.channel_phone.id,
            }
        )

    def test_partner_communication_channel(self):
        sale = self.env["sale.order"].create(
            {
                "partner_id": self.partner_1.id,
            }
        )
        self.assertEqual(
            sale.partner_communication_channel_id,
            self.channel_email,
        )

    def test_change_partner_updates_communication_channel(self):
        sale = self.env["sale.order"].create(
            {
                "partner_id": self.partner_1.id,
            }
        )
        sale.partner_id = self.partner_2
        self.assertEqual(
            sale.partner_communication_channel_id,
            self.channel_phone,
        )

    def test_communication_channel_can_be_changed_manually(self):
        sale = self.env["sale.order"].create(
            {
                "partner_id": self.partner_1.id,
            }
        )
        sale.partner_communication_channel_id = self.channel_phone
        self.assertEqual(
            sale.partner_communication_channel_id,
            self.channel_phone,
        )
        self.assertEqual(
            self.partner_1.partner_communication_channel_id,
            self.channel_email,
        )

    def test_partner_without_communication_channel(self):
        partner = self.env["res.partner"].create(
            {
                "name": "Partner without channel",
            }
        )
        sale = self.env["sale.order"].create(
            {
                "partner_id": partner.id,
            }
        )
        self.assertFalse(sale.partner_communication_channel_id)
