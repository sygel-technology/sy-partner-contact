# Copyright 2024 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import _, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    def create(self, vals_list):
        res = super().create(vals_list)
        if not self.env.context.get("skip_partner_children_address_autocreate"):
            vals_aux = [
                {"name": _("Invoice Addr."), "type": "invoice"},
                {"name": _("Delivery Addr."), "type": "delivery"},
            ]
            for r in res.filtered(lambda x: x.is_company):
                vals_contact = {
                    "street": r.street,
                    "street2": r.street2,
                    "city": r.city,
                    "state_id": r.state_id.id,
                    "zip": r.zip,
                    "zip_id": r.zip_id.id,
                    "country_id": r.country_id.id,
                    "lang": r.lang,
                    "user_id": r.user_id.id,
                    "company_type": "person",
                    "parent_id": r.id,
                    "phone": r.phone,
                    "website": r.website,
                    "category_id": [(6, 0, r.category_id.ids)],
                }
                for val_cont in vals_aux:
                    val_cont.update(vals_contact)
                    r.create(val_cont)
        return res
