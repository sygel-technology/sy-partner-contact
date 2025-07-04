from odoo.tests.common import TransactionCase


class TestPartnerPrivateInformationAutocomplete(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.country = cls.env["res.country"].create(
            {
                "name": "Test Country",
                "code": "TestC",
            }
        )

        cls.state = cls.env["res.country.state"].create(
            {
                "name": "Test State",
                "code": "TS",
                "country_id": cls.country.id,
            }
        )

        cls.city = cls.env["res.city"].create(
            {
                "name": "Test City",
                "state_id": cls.state.id,
                "country_id": cls.country.id,
            }
        )

        cls.zip = cls.env["res.city.zip"].create(
            {
                "name": "12345",
                "city_id": cls.city.id,
                "state_id": cls.state.id,
                "country_id": cls.country.id,
            }
        )

        cls.partner = cls.env["res.partner"].create(
            {
                "name": "Test Partner",
                "private_zip_id": cls.zip.id,
            }
        )

    def test_compute_private_zip_id(self):
        self.partner.private_zip = "12345"
        self.partner._compute_private_zip_id()
        self.assertEqual(self.partner.private_zip_id, self.zip)

    def test_compute_private_city_id(self):
        self.partner.private_zip_id = self.zip
        self.partner._compute_private_city_id()
        self.assertEqual(self.partner.private_city_id, self.city)

    def test_compute_private_city(self):
        self.partner.private_zip_id = self.zip
        self.partner._compute_private_city()
        self.assertEqual(self.partner.private_city, self.city.name)

    def test_compute_private_zip(self):
        self.partner.private_zip_id = self.zip
        self.partner._compute_private_zip()
        self.assertEqual(self.partner.private_zip, self.zip.name)

    def test_compute_private_country_id(self):
        self.partner.private_zip_id = self.zip
        self.partner._compute_private_country_id()
        self.assertEqual(self.partner.private_country_id, self.country)

    def test_compute_private_state_id(self):
        self.partner.private_zip_id = self.zip
        self.partner._compute_private_state_id()
        self.assertEqual(self.partner.private_state_id, self.state)

    def test_address_fields(self):
        address_fields = self.partner._address_fields()
        self.assertIn("private_zip_id", address_fields)
        self.assertIn("private_city_id", address_fields)
