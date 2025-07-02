from odoo import fields
from odoo.tests.common import TransactionCase


class TestPartnerCodeProgramSale(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.code_program_territory = cls.env[
            "res.partner.code.program.territory"
        ].create(
            {
                "name": "Territory test",
                "code": "CPT-001",
            }
        )

        cls.partner = cls.env["res.partner"].create(
            {
                "name": "Partner test",
                "code_program_territory_id": cls.code_program_territory.id,
            }
        )

        cls.sale_report = cls.env["sale.report"]

    def test_code_program_territory_id(self):
        self.assertIn("code_program_territory_id", self.sale_report._fields)

    def test_code_program_territory_id_in_select_additional_fields(self):
        fields = self.env["sale.report"]._select_additional_fields()
        self.assertIn("code_program_territory_id", fields)
        self.assertEqual(
            fields["code_program_territory_id"], "partner.code_program_territory_id"
        )

    def test_code_program_territory_id_in_group_by(self):
        group_by = self.env["sale.report"]._group_by_sale()
        self.assertIn("partner.code_program_territory_id", group_by)

    def test_sale_inherits_code_program_territory(self):
        sale_order = self.env["sale.order"].create(
            {
                "partner_id": self.partner.id,
                "date_order": fields.Date.today(),
            }
        )
        self.assertEqual(
            sale_order.partner_id.code_program_territory_id,
            self.code_program_territory,
            "The sale order's partner should have the expected code program territory",
        )
