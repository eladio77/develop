from odoo import fields, models, api


class ModelName(models.Model):
    _name = 'library.checkout'
    _description = 'Checkout request'

    member_id = fields.Many2one(
        "library.member", required=True
    )

    user_id = fields.Many2one(
        "res.users", "Libreria",
        default=lambda s: s.env.user,
    )

    request_date = fields.Date(default=lambda s: fields.Date.today())
