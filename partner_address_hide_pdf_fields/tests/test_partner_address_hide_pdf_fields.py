from odoo_test_helper import FakeModelLoader

from odoo.tests.common import TransactionCase


class TestPartnerAddressHidePdfFields(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.loader = FakeModelLoader(cls.env, cls.__module__)
        cls.loader.backup_registry()
        from .fake_models import ResPartner

        cls.loader.update_registry((ResPartner,))

        cls.partner = cls.env["res.partner"].create(
            {
                "name": "Partner Test",
                "city": "Test City",
                "zip": "12345",
                "street": "Test Street",
            }
        )

    @classmethod
    def tearDownClass(cls):
        cls.loader.restore_registry()
        super().tearDownClass()

    def test_fields_hidden_inside_pdf(self):
        partner_ctx = self.partner.with_context(inside_pdf=True)
        _, args = partner_ctx._prepare_display_address()
        self.assertEqual(args["field_id"], "")
        self.assertEqual(args["field_name"], "")

    def test_fields_visible_outside_pdf(self):
        _, args = self.partner._prepare_display_address()
        self.assertEqual(args["field_id"], "123")
        self.assertEqual(args["field_name"], "Field Name")
