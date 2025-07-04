from odoo.exceptions import AccessError
from odoo.tests.common import TransactionCase, new_test_user


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
            _ = partner.private_email

    def test_private_fields_default_values(self):
        self.assertFalse(self.partner.private_phone)
        self.assertFalse(self.partner.private_email)
