# Copyright 2024 Ángel García de la Chica Herrera <angel.garcia@sygel.es>
# License AGPL-3 - See https://www.gnu.org/licenses/agpl-3.0

from odoo.tests import common


class TestPartnerDisableVatVerification(common.TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        for country_id in cls.env["res.country"].search([]):
            cls.env["res.partner"].create(
                {
                    "name": f"Test {country_id.code}",
                    "country_id": country_id.id,
                }
            )

    def test_vat_modification_existing_contact(self):
        for partner in self.env["res.partner"].search([]):
            partner.write({"vat": "1234¿?"})

    def test_vat_new_contact(self):
        for country_id in self.env["res.country"].search([]):
            self.env["res.partner"].create(
                {
                    "name": f"Test_2 {country_id.code}",
                    "country_id": country_id.id,
                    "vat": "1234¿?",
                }
            )
