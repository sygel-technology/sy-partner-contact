from odoo import fields
from odoo.tests.common import TransactionCase


class TestPartnerCodeProgramPurchase(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.partner_code_program = cls.env["res.partner.code.program"].create(
            {
                "name": "Program test",
                "code": "CP-001",
            }
        )

        cls.partner = cls.env["res.partner"].create(
            {
                "name": "Partner test",
                "code_program_id": cls.partner_code_program.id,
            }
        )

        cls.purchase_report = cls.env["purchase.report"]

    def test_code_program_id(self):
        self.assertIn("code_program_id", self.purchase_report._fields)

    def test_select(self):
        self.assertIn(
            "partner.code_program_id as code_program_id",
            str(self.purchase_report._select()),
        )

    def test_group_by(self):
        self.assertIn("partner.code_program_id", str(self.purchase_report._group_by()))

    def test_purchase_inherits_code_program(self):
        purchase_order = self.env["purchase.order"].create(
            {
                "partner_id": self.partner.id,
                "date_order": fields.Date.today(),
                "order_line": [],
            }
        )
        self.assertEqual(
            purchase_order.partner_id.code_program_id,
            self.partner_code_program,
            "Purchase order partner should have the same code program",
        )
