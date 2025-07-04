from odoo.tests.common import TransactionCase


class TestPartnerAddressHidePdfFields(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.partner = cls.env["res.partner"].create(
            {
                "name": "Test Partner",
                "country_id": cls.env.ref("base.es").id,
                "city": "Test city",
                "zip": "12345",
                "street": "Test street",
            }
        )

        cls._original_hided = cls.env[
            "res.partner"
        ].__class__._hided_in_pdf_address_fields

        def fake_hided_in_pdf_address_fields(cls):
            return ["field_id", "field_name"]

        cls.env["res.partner"].__class__._hided_in_pdf_address_fields = classmethod(
            fake_hided_in_pdf_address_fields
        )

        cls._original_prepare = cls.env[
            "res.partner"
        ].__class__._prepare_display_address

        def test_prepare_display_address(self, without_company=False):
            address_format, args = cls._original_prepare(self, without_company)
            args.update({"field_id": "123", "field_name": "Name"})
            if self._display_address_inside_pdf():
                args.update({key: "" for key in self._hided_in_pdf_address_fields()})
            return address_format, args

        cls.env[
            "res.partner"
        ].__class__._prepare_display_address = test_prepare_display_address

    @classmethod
    def tearDownClass(cls):
        cls.env[
            "res.partner"
        ].__class__._hided_in_pdf_address_fields = cls._original_hided
        cls.env[
            "res.partner"
        ].__class__._prepare_display_address = cls._original_prepare
        super().tearDownClass()

    def test_fields_hidden_inside_pdf(self):
        partner_with_ctx = self.partner.with_context(inside_pdf=True)
        _, args = partner_with_ctx._prepare_display_address()
        self.assertEqual(args.get("field_id"), "")
        self.assertEqual(args.get("field_name"), "")

    def test_fields_visible_outside_pdf(self):
        _, args = self.partner._prepare_display_address()
        self.assertEqual(args.get("field_id"), "123")
        self.assertEqual(args.get("field_name"), "Name")
