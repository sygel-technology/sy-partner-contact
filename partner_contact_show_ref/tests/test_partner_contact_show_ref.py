# Copyright 2025 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo.tests.common import TransactionCase


class TestPartnerContactShowRef(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        partner_model = cls.env["res.partner"]
        cls.test_company = partner_model.create(
            {"name": "Test Company", "company_type": "company"}
        )
        cls.test_person = partner_model.create(
            {
                "name": "Test Person",
                "parent_id": cls.test_company.id,
                "company_type": "person",
            }
        )

    def test_partner_contact_show_ref(self):
        ref = "Fer"
        self.test_company.ref = ref
        self.assertIn(ref, self.test_person.display_name)
        self.assertIn(ref, self.test_company.display_name)

    def test_partner_contact_show_own_ref(self):
        ref1 = "Fer1"
        ref2 = "Fer2"
        self.test_company.ref = ref1
        self.test_person.own_ref_in_name = True
        self.assertNotIn(ref1, self.test_person.display_name)
        self.test_person.ref = ref2
        self.test_person._compute_display_name()
        self.assertIn(ref2, self.test_person.display_name)
