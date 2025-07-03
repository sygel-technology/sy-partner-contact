from odoo.tests.common import TransactionCase


class TestPartnerCodeProgramTerritoryHidePdfFields(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.partner_model = cls.env["res.partner"]

    def test_hided_in_pdf_address_fields(self):
        hidden_fields = self.partner_model._hided_in_pdf_address_fields()
        self.assertIn("code_program_territory_id", hidden_fields)
        self.assertIn("code_program_territory_name", hidden_fields)
