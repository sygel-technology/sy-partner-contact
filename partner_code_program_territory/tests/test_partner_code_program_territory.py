from odoo.tests import Form
from odoo.tests.common import TransactionCase


class TestPartnerCodeProgramTerritory(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.code_program_1 = cls.env["res.partner.code.program"].create(
            {
                "name": "Code Program 1",
                "code": "CP-001",
            }
        )

        cls.code_program_2 = cls.env["res.partner.code.program"].create(
            {
                "name": "Code Program 2",
                "code": "CP-002",
            }
        )

        cls.code_program_territory_1 = cls.env[
            "res.partner.code.program.territory"
        ].create(
            {
                "name": "Territory 1",
                "code": "CPT-001",
                "code_program_id": cls.code_program_1.id,
            }
        )

        cls.code_program_territory_2 = cls.env[
            "res.partner.code.program.territory"
        ].create(
            {
                "name": "Territory 2",
                "code": "CPT-002",
                "code_program_id": cls.code_program_2.id,
            }
        )

        cls.partner_1 = cls.env["res.partner"].create(
            {
                "name": "Partner 1",
                "code_program_id": cls.code_program_1.id,
                "code_program_territory_id": cls.code_program_territory_1.id,
            }
        )

        cls.partner_2 = cls.env["res.partner"].create(
            {
                "name": "Partner 2",
                "code_program_id": cls.code_program_2.id,
                "code_program_territory_id": cls.code_program_territory_2.id,
            }
        )

    def test_compute_res_partner_count(self):
        self.code_program_territory_1._compute_res_partner_count()
        self.assertEqual(self.code_program_territory_1.res_partner_count, 1)

    def test_compute_code_terriroty_count(self):
        self.code_program_1._compute_code_terriroty_count()
        self.assertEqual(self.code_program_1.code_terriroty_count, 1)
        self.code_program_2._compute_code_terriroty_count()
        self.assertEqual(self.code_program_2.code_terriroty_count, 1)

    def test_onchange_code_program_id(self):
        self.partner_1.code_program_id = self.code_program_1
        self.partner_1.code_program_territory_id = self.code_program_territory_1
        with Form(self.partner_1) as f:
            f.code_program_id = self.code_program_2
        self.assertFalse(self.partner_1.code_program_territory_id)

    def test_onchange_code_program_territory_id(self):
        with Form(self.partner_1) as f:
            f.code_program_id = self.code_program_1
            f.code_program_territory_id = self.code_program_territory_2
        self.assertEqual(
            self.partner_1.code_program_id,
            self.code_program_territory_2.code_program_id,
        )

    def test_address_fields(self):
        partner_model = self.env["res.partner"]
        fields = partner_model._address_fields()
        self.assertIn("code_program_territory_id", fields)
        self.assertIn("code_program_territory_name", fields)

    def test_commercial_fields(self):
        partner_model = self.env["res.partner"]
        fields = partner_model._commercial_fields()
        self.assertIn("code_program_territory_id", fields)
