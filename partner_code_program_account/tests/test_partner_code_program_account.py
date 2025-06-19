from odoo.tests.common import TransactionCase


class TestPartnerCodeProgramAccount(TransactionCase):
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

        cls.invoice_report = cls.env["account.invoice.report"]

    def test_code_program_id(self):
        invoice = self.env["account.move"].create(
            {
                "partner_id": self.partner.id,
                "move_type": "out_invoice",
            }
        )
        self.assertEqual(invoice.code_program_id, self.partner_code_program)

    def test_select(self):
        report = self.env["account.invoice.report"]
        select = report._select()
        self.assertIn("partner.code_program_id AS code_program_id", str(select))
