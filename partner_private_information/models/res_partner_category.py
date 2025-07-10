from odoo import fields, models


class ResPartnerCategory(models.Model):
    _inherit = "res.partner.category"

    is_private = fields.Boolean(string="Private Category", default=False)
