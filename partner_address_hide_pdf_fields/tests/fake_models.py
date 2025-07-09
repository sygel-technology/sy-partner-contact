from odoo import models


class ResPartner(models.Model):
    _name = "res.partner"
    _inherit = "res.partner"
    _description = "Fake ResPartner for Testing"

    def _hided_in_pdf_address_fields(self):
        return super()._hided_in_pdf_address_fields() + ["field_id", "field_name"]

    # This FakeModel overrides `_prepare_display_address` to simulate
    # additional address fields (`field_id`, `field_name`) being included
    # and hidden depending on the `inside_pdf` context.
    def _prepare_display_address(self, without_company=False):
        address_format, args = super()._prepare_display_address(without_company)
        args.update({"field_id": "123", "field_name": "Field Name"})
        if self._display_address_inside_pdf():
            args.update({key: "" for key in self._hided_in_pdf_address_fields()})
        return address_format, args
