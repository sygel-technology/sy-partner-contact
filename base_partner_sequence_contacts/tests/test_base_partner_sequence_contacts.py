# Copyright 2026 Ángel Rivas <angel.rivas@sygel.es>
# License AGPL-3 - See https://www.gnu.org/licenses/agpl-3.0


from odoo.tests.common import TransactionCase


class TestBasePartnerSequenceAll(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.Partner = cls.env["res.partner"]

    def test_child_partner_gets_own_ref(self):
        parent = self.Partner.create(
            {
                "name": "Parent Company",
                "is_company": True,
            }
        )
        child = self.Partner.create(
            {
                "name": "Child Contact",
                "parent_id": parent.id,
            }
        )
        self.assertTrue(parent.ref)
        self.assertTrue(child.ref)
        self.assertNotEqual(parent.ref, child.ref)

    def test_children_get_different_refs(self):
        parent = self.Partner.create(
            {
                "name": "Parent Company",
                "is_company": True,
            }
        )
        child_1 = self.Partner.create(
            {
                "name": "Child 1",
                "parent_id": parent.id,
            }
        )
        child_2 = self.Partner.create(
            {
                "name": "Child 2",
                "parent_id": parent.id,
            }
        )
        self.assertNotEqual(child_1.ref, child_2.ref)

    def test_parent_ref_is_not_propagated_to_child(self):
        parent = self.Partner.create(
            {
                "name": "Parent Company",
                "is_company": True,
            }
        )
        child = self.Partner.create(
            {
                "name": "Child Contact",
                "parent_id": parent.id,
            }
        )
        child_ref = child.ref
        parent.ref = "NEW-PARENT-REF"
        self.assertEqual(child.ref, child_ref)
