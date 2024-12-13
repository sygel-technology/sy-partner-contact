# Copyright 2024 Alberto Martínez <alberto.martinez@sygel.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    grandchild_ids = fields.One2many(
        comodel_name="res.partner",
        string="SubContacts",
        compute="_compute_grandchild_ids",
    )

    def _calculate_subchilds(self, child_list):
        child_list_obj = self.env["res.partner"].browse(child_list)
        n_child_list = child_list
        for child in child_list_obj:
            if child.child_ids:
                n_child_list += self._calculate_subchilds(child.child_ids.ids)
        return n_child_list

    @api.depends("child_ids", "child_ids.child_ids")
    def _compute_grandchild_ids(self):
        subchild_list = []
        for child in self.child_ids:
            if child.child_ids:
                subchild_list += child._calculate_subchilds(child.child_ids.ids)
        subchild_objs = self.env["res.partner"].browse(subchild_list)
        self.grandchild_ids += subchild_objs
