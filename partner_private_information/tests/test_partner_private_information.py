from odoo.exceptions import AccessError, ValidationError
from odoo.tests.common import Form, TransactionCase, new_test_user


class TestPartnerPrivateInformation(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.user_private = new_test_user(
            cls.env,
            login="user_private_info",
            groups="base.group_user,base.group_partner_manager,partner_private_information.group_partner_private_info",
        )

        cls.user_public = new_test_user(
            cls.env, login="user_public_info", groups="base.group_user"
        )

        cls.partner = cls.env["res.partner"].create(
            {
                "name": "Test Partner",
            }
        )

    def test_private_fields_visible_to_authorized_user(self):
        partner = self.partner.with_user(self.user_private)
        partner.write(
            {
                "private_phone": "123456789",
                "private_email": "private@example.com",
            }
        )
        self.assertEqual(partner.private_phone, "123456789")
        self.assertEqual(partner.private_email, "private@example.com")

    def test_private_fields_hidden_from_unauthorized_user(self):
        partner = self.partner.with_user(self.user_public)

        with self.assertRaises(AccessError):
            _ = partner.private_phone
        with self.assertRaises(AccessError):
            _ = partner.private_email

    def test_private_fields_default_values(self):
        self.assertFalse(self.partner.private_phone)
        self.assertFalse(self.partner.private_email)

    def test_invalid_private_phone_format(self):
        partner = self.partner.with_user(self.user_private)
        with self.assertRaises(ValidationError):
            partner.private_phone = "abc123"
            partner._check_internal_contact_info_format()

    def test_invalid_private_mobile_format(self):
        partner = self.partner.with_user(self.user_private)
        with self.assertRaises(ValidationError):
            partner.write({"private_mobile": "invalid_mobile!"})

    def test_invalid_private_email_format(self):
        partner = self.partner.with_user(self.user_private)
        with self.assertRaises(ValidationError):
            partner.write({"private_email": "notanemail@com"})

    def test_valid_private_contact_info(self):
        partner = self.partner.with_user(self.user_private)
        partner.write(
            {
                "private_phone": "+34 912 345 678",
                "private_mobile": "601-602-603",
                "private_email": "john.doe@example.com",
            }
        )

    def test_onchange_private_phone_with_form(self):
        partner = self.partner.with_user(self.user_private)
        with Form(partner) as form:
            form.private_phone = "+34123456789"
        self.assertTrue(partner.private_phone.startswith("+"))

    def test_onchange_private_mobile_with_form(self):
        partner = self.partner.with_user(self.user_private)
        with Form(partner) as form:
            form.private_mobile = "+34600100200"
        self.assertTrue(partner.private_mobile.startswith("+"))
