from odoo import fields
from odoo.tests.common import TransactionCase


class TestPartnerCodeProgramTerritoryPurchase(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.code_program_territory = cls.env[
            "res.partner.code.program.territory"
        ].create(
            {
                "name": "Territory Test",
                "code": "CPT-TEST",
            }
        )
        cls.partner = cls.env["res.partner"].create(
            {
                "name": "Partner Test",
                "code_program_territory_id": cls.code_program_territory.id,
            }
        )

        cls.purchase_report = cls.env["purchase.report"]

    def test_code_program_territory_id(self):
        self.assertIn("code_program_territory_id", self.purchase_report._fields)

    def test_select(self):
        self.assertIn(
            "partner.code_program_territory_id as code_program_territory_id",
            str(self.purchase_report._select()),
        )

    def test_group_by(self):
        self.assertIn(
            "partner.code_program_territory_id", str(self.purchase_report._group_by())
        )

    def test_purchase_inherits_code_program(self):
        purchase_order = self.env["purchase.order"].create(
            {
                "partner_id": self.partner.id,
                "date_order": fields.Date.today(),
            }
        )
        self.assertEqual(
            purchase_order.partner_id.code_program_territory_id,
            self.code_program_territory,
            "Purchase order partner should have the same code program territory",
        )
