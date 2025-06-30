from odoo.tests.common import TransactionCase


class TestPartnerIndustrialEstate(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.industrial_estate = cls.env["res.partner.industrial.estate"].create(
            {
                "name": "Industrial Estate Test",
                "code": "IE-001",
            }
        )

        cls.partner = cls.env["res.partner"].create(
            {
                "name": "Partner Test",
                "industrial_estate_id": cls.industrial_estate.id,
            }
        )

    def test_address_fields(self):
        address_fields = self.partner._address_fields()
        self.assertIn("industrial_estate_id", address_fields)
        self.assertIn("industrial_estate_name", address_fields)

    def test_commercial_fields(self):
        commercial_fields = self.partner._commercial_fields()
        self.assertIn("industrial_estate_id", commercial_fields)

    def test_compute_res_partner_count(self):
        self.industrial_estate._compute_res_partner_count()
        self.assertEqual(self.industrial_estate.res_partner_count, 1)

    def test_action_view_res_partner(self):
        action = self.industrial_estate.action_view_res_partner()
        self.assertEqual(action["res_model"], "res.partner")
        self.assertIn(
            ("industrial_estate_id", "=", self.industrial_estate.id), action["domain"]
        )
