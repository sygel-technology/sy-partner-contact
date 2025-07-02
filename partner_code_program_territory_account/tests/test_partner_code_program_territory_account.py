from odoo.tests.common import TransactionCase


class TestPartnerCodeProgramTerritoryAccount(TransactionCase):
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

        cls.invoice_report = cls.env["account.invoice.report"]

    def test_code_program_territory_id_field_exists(self):
        fields_list = self.env["account.invoice.report"].fields_get()
        self.assertIn("code_program_territory_id", fields_list)

    def test_select(self):
        report = self.env["account.invoice.report"]
        select = report._select()
        self.assertIn(
            "partner.code_program_territory_id AS code_program_territory_id",
            str(select),
        )

    def test_invoice_territory(self):
        invoice = self.env["account.move"].create(
            {
                "partner_id": self.partner.id,
                "move_type": "out_invoice",
            }
        )
        self.assertEqual(
            invoice.code_program_territory_id, self.partner.code_program_territory_id
        )
