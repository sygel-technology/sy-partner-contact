# Copyright 2025 Ángel Rivas <angel.rivas@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo.tests.common import TransactionCase


class TestPartnerTags(TransactionCase):
    def setUp(self):
        super().setUp()
        self.category1 = self.env["res.partner.category"].create({"name": "Category 1"})
        self.category2 = self.env["res.partner.category"].create({"name": "Category 2"})

        self.parent1 = self.env["res.partner"].create(
            {
                "name": "Parent 1",
                "is_company": True,
                "category_id": [(6, 0, [self.category1.id])],
            }
        )

        self.parent2 = self.env["res.partner"].create(
            {
                "name": "Parent 2",
                "is_company": True,
                "category_id": [(6, 0, [self.category2.id])],
            }
        )

    def test_create_partner_with_parent_tags(self):
        partner = self.env["res.partner"].create(
            {"name": "Child Partner", "is_company": False, "parent_id": self.parent1.id}
        )

        self.assertEqual(len(partner.category_id), 1)
        self.assertEqual(partner.category_id, self.parent1.category_id)

    def test_create_partner_without_parent_tags(self):
        partner = self.env["res.partner"].create(
            {
                "name": "Child Partner 2",
                "is_company": False,
            }
        )

        self.assertEqual(len(partner.category_id), 0)

    def test_change_parent_does_not_change_tags(self):
        partner = self.env["res.partner"].create(
            {
                "name": "Child Partner 3",
                "is_company": False,
                "parent_id": self.parent1.id,
            }
        )

        self.assertEqual(len(partner.category_id), 1)
        self.assertEqual(partner.category_id, self.parent1.category_id)

        partner.parent_id = self.parent2

        self.assertEqual(len(partner.category_id), 1)
        self.assertEqual(partner.category_id, self.parent1.category_id)

    def test_create_partner_with_parent_and_categories(self):
        parent = self.env["res.partner"].create(
            {
                "name": "Parent",
                "is_company": True,
                "category_id": [(6, 0, [self.category1.id, self.category2.id])],
            }
        )

        partner = self.env["res.partner"].create(
            {
                "name": "Child",
                "is_company": False,
                "parent_id": parent.id,
                "category_id": [(6, 0, [self.category1.id])],
            }
        )

        self.assertEqual(len(partner.category_id), 2)
        self.assertIn(self.category1, partner.category_id)
        self.assertIn(self.category2, partner.category_id)
