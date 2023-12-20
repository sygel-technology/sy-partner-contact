# Copyright 2023 Manuel Regidor <manuel.regidor@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, exceptions, api, _


class ResPartner(models.Model):
    _inherit = "res.partner"

    def _needs_ref(self, vals=None):
        if not vals and not self:  # pragma: no cover
            raise exceptions.UserError(
                _("Either field values or an id must be provided.")
            )
        return True

    @api.model
    def _commercial_fields(self):
        fields = super()._commercial_fields()
        if fields and "ref" in fields:
            fields.remove("ref")
        return fields
