# Copyright 2026 Ángel Rivas <angel.rivas@sygel.es>
# License AGPL-3 - See https://www.gnu.org/licenses/agpl-3.0
from odoo.tests.common import TransactionCase


class TestPartnerInvoicingFrequency(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.frequency_weekly = cls.env["partner.invoicing.frequency"].create(
            {
                "name": "Weekly",
            }
        )
        cls.frequency_monthly = cls.env["partner.invoicing.frequency"].create(
            {
                "name": "Monthly",
            }
        )
        cls.partner_1 = cls.env["res.partner"].create(
            {
                "name": "Partner 1",
                "partner_invoicing_frequency_id": cls.frequency_weekly.id,
            }
        )
        cls.partner_2 = cls.env["res.partner"].create(
            {
                "name": "Partner 2",
                "partner_invoicing_frequency_id": cls.frequency_monthly.id,
            }
        )

    def test_partner_invoicing_frequency_from_partner(self):
        sale = self.env["sale.order"].create(
            {
                "partner_id": self.partner_1.id,
            }
        )
        self.assertEqual(
            sale.partner_invoicing_frequency_id,
            self.frequency_weekly,
        )

    def test_change_partner_updates_invoicing_frequency(self):
        sale = self.env["sale.order"].create(
            {
                "partner_id": self.partner_1.id,
            }
        )
        sale.partner_id = self.partner_2
        self.assertEqual(
            sale.partner_invoicing_frequency_id,
            self.frequency_monthly,
        )

    def test_invoicing_frequency_can_be_changed_manually(self):
        sale = self.env["sale.order"].create(
            {
                "partner_id": self.partner_1.id,
            }
        )
        sale.partner_invoicing_frequency_id = self.frequency_monthly
        self.assertEqual(
            sale.partner_invoicing_frequency_id,
            self.frequency_monthly,
        )
        self.assertEqual(
            self.partner_1.partner_invoicing_frequency_id,
            self.frequency_weekly,
        )

    def test_partner_without_invoicing_frequency(self):
        partner = self.env["res.partner"].create(
            {
                "name": "Partner without invoicing frequency",
            }
        )
        sale = self.env["sale.order"].create(
            {
                "partner_id": partner.id,
            }
        )
        self.assertFalse(sale.partner_invoicing_frequency_id)

    def test_invoicing_frequency_is_commercial_field(self):
        contact = self.env["res.partner"].create(
            {
                "name": "Contact",
                "parent_id": self.partner_1.id,
            }
        )
        self.assertEqual(
            contact.partner_invoicing_frequency_id,
            self.frequency_weekly,
        )
