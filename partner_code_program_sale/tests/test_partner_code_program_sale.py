from odoo import fields
from odoo.tests.common import TransactionCase


class TestPartnerCodeProgramSale(TransactionCase):
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

        cls.sale_report = cls.env["sale.report"]

    def test_code_program_id(self):
        self.assertIn("code_program_id", self.sale_report._fields)

    def test_code_program_id_in_select_additional_fields(self):
        fields = self.env["sale.report"]._select_additional_fields()
        self.assertIn("code_program_id", fields)
        self.assertEqual(fields["code_program_id"], "partner.code_program_id")

    def test_code_program_id_in_group_by(self):
        group_by = self.env["sale.report"]._group_by_sale()
        self.assertIn("partner.code_program_id", group_by)

    def test_sale_inherits_code_program(self):
        sale_order = self.env["sale.order"].create(
            {
                "partner_id": self.partner.id,
                "date_order": fields.Date.today(),
                "order_line": [],
            }
        )
        self.assertEqual(
            sale_order.partner_id.code_program_id,
            self.partner_code_program,
            "The sale order should inherit the code program from the partner",
        )
