# Copyright 2026 Ángel Rivas <angel.rivas@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo.tests import TransactionCase


class TestPartnerGuild(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.guild = cls.env["res.partner.guild"].create(
            {
                "name": "Construction",
            }
        )
        cls.company = cls.env["res.partner"].create(
            {
                "name": "Test Company",
                "is_company": True,
                "guild_ids": [(6, 0, cls.guild.ids)],
            }
        )
        cls.contact = cls.env["res.partner"].create(
            {
                "name": "Test Contact",
                "parent_id": cls.company.id,
            }
        )

    def test_guild_creation(self):
        self.assertEqual(self.guild.name, "Construction")
        self.assertTrue(self.guild.active)

    def test_guild_copy(self):
        guild_copy = self.guild.copy()
        self.assertEqual(guild_copy.name, "Construction (copy)")
        self.assertTrue(guild_copy.active)

    def test_guild_commercial_field(self):
        self.assertIn("guild_ids", self.company._commercial_fields())

    def test_contact_inherits_guilds(self):
        self.assertEqual(self.contact.guild_ids, self.company.guild_ids)

    def test_update_company_guilds_propagates_to_contact(self):
        new_guild = self.env["res.partner.guild"].create(
            {
                "name": "Automotive",
            }
        )
        self.company.guild_ids = new_guild
        self.assertEqual(self.contact.guild_ids, new_guild)

    def test_new_contact_inherits_company_guilds(self):
        contact = self.env["res.partner"].create(
            {
                "name": "Second Test Contact",
                "parent_id": self.company.id,
            }
        )
        self.assertEqual(contact.guild_ids, self.company.guild_ids)
