from odoo.tests import Form
from odoo.tests.common import TransactionCase


class TestBaseLocationCodeProgramTerritory(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.code_program = cls.env["res.partner.code.program"].create(
            {
                "name": "Program test",
                "code": "CP-001",
            }
        )

        cls.code_program_2 = cls.env["res.partner.code.program"].create(
            {
                "name": "Program test 2",
                "code": "CP-002",
            }
        )

        cls.code_program_territory = cls.env[
            "res.partner.code.program.territory"
        ].create(
            {
                "name": "Territory test",
                "code": "CPT-001",
                "code_program_id": cls.code_program.id,
            }
        )

        cls.partner = cls.env["res.partner"].create(
            {
                "name": "Partner test",
                "code_program_territory_id": cls.code_program_territory.id,
            }
        )

        cls.country = cls.env["res.country"].create(
            {
                "name": "Country test",
                "code": "CT",
            }
        )

        cls.state = cls.env["res.country.state"].create(
            {
                "name": "State test",
                "code": "ST",
                "country_id": cls.country.id,
            }
        )

        cls.city = cls.env["res.city"].create(
            {
                "name": "City test",
                "state_id": cls.state.id,
                "country_id": cls.country.id,
            }
        )

        cls.zip = cls.env["res.city.zip"].create(
            {
                "name": "1001",
                "city_id": cls.city.id,
                "state_id": cls.state.id,
                "country_id": cls.country.id,
                "code_program_id": cls.code_program.id,
                "code_program_territory_id": cls.code_program_territory.id,
            }
        )

    def test_onchange_code_program_id(self):
        self.zip.code_program_territory_id = self.code_program_territory
        with Form(self.zip) as f:
            f.code_program_id = self.code_program_2
        self.assertFalse(self.zip.code_program_territory_id)

    def test_onchange_code_program_territory_id(self):
        self.zip.code_program_id = self.code_program_2
        with Form(self.zip) as f:
            f.code_program_territory_id = self.code_program_territory
        self.assertEqual(self.zip.code_program_id, self.code_program)

    def test_compute_display_name(self):
        # Code_program_territory_id and code_program_id are defined
        self.zip.code_program_id = self.code_program
        self.zip.code_program_territory_id = self.code_program_territory
        self.zip._compute_display_name()

        # Check that all fragments are in display_name
        display_name = self.zip.display_name
        self.assertIn(self.code_program_territory.name, display_name)
        self.assertIn(self.code_program.name, display_name)
        self.assertIn(self.country.name, display_name)

        # Check that they appear in order: Territory, Program, Country
        pos_territory = display_name.find(self.code_program_territory.name)
        pos_program = display_name.find(self.code_program.name)
        pos_country = display_name.find(self.country.name)

        self.assertTrue(
            pos_territory < pos_program < pos_country,
            msg=f"Order incorrect in display_name: {display_name}",
        )

        # Only code_program_territory_id is defined
        self.zip.code_program_id = False
        self.zip._compute_display_name()

        display_name = self.zip.display_name
        self.assertIn(self.code_program_territory.name, display_name)
        self.assertIn(self.country.name, display_name)
        self.assertNotIn(self.code_program.name, display_name)

        pos_territory = display_name.find(self.code_program_territory.name)
        pos_country = display_name.find(self.country.name)
        self.assertTrue(
            pos_territory < pos_country,
            msg=f"Order incorrect in display_name: {display_name}",
        )

        # Only code_program_id is defined
        self.zip.code_program_territory_id = False
        self.zip.code_program_id = self.code_program
        self.zip._compute_display_name()

        display_name = self.zip.display_name
        self.assertIn(self.code_program.name, display_name)
        self.assertIn(self.country.name, display_name)
        self.assertNotIn(self.code_program_territory.name, display_name)

        pos_program = display_name.find(self.code_program.name)
        pos_country = display_name.find(self.country.name)
        self.assertTrue(
            pos_program < pos_country,
            msg=f"Order incorrect in display_name: {display_name}",
        )

        # None of the fields is defined
        self.zip.write(
            {
                "code_program_territory_id": False,
                "code_program_id": False,
            }
        )
        self.zip.invalidate_recordset(["code_program_id", "code_program_territory_id"])
        self.zip._compute_display_name()
        display_name = self.zip.display_name
        self.assertIn(self.country.name, display_name)
        self.assertNotIn(self.code_program.name, display_name)
        self.assertNotIn(self.code_program_territory.name, display_name)

    def test_compute_code_program_id(self):
        with Form(self.partner) as f:
            f.zip_id = self.zip
        self.assertEqual(self.partner.code_program_id, self.zip.code_program_id)
        original_code_program_id = self.partner.code_program_id
        self.partner.write({"zip_id": False})
        self.assertEqual(self.partner.code_program_id, original_code_program_id)

    def test_compute_code_program_territory_id(self):
        with Form(self.partner) as f:
            f.zip_id = self.zip
        self.assertEqual(
            self.partner.code_program_territory_id, self.zip.code_program_territory_id
        )
        original_code_program_territory_id = self.partner.code_program_territory_id
        self.partner.write({"zip_id": False})
        self.assertEqual(
            self.partner.code_program_territory_id, original_code_program_territory_id
        )
