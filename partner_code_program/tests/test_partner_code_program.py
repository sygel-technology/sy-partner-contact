from odoo.tests.common import TransactionCase


class TestPartnerCodeProgram(TransactionCase):
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

    def test_address_fields(self):
        address_fields = self.partner._address_fields()
        self.assertIn("code_program_id", address_fields)
        self.assertIn("code_program_name", address_fields)

    def test_commercial_fields(self):
        commercial_fields = self.partner._commercial_fields()
        self.assertIn("code_program_id", commercial_fields)

    def test_compute_res_partner_count(self):
        self.partner_code_program._compute_res_partner_count()
        self.assertEqual(self.partner_code_program.res_partner_count, 1)

    def test_action_view_res_partner(self):
        action = self.partner_code_program.action_view_res_partner()
        self.assertEqual(action["res_model"], "res.partner")
        self.assertIn(
            ("code_program_id", "=", self.partner_code_program.id), action["domain"]
        )
