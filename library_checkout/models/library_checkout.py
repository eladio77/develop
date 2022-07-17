from odoo import fields, models, api


class Checkout(models.Model):
    _name = "library.checkout"
    _description = 'Checkout request'

    member_id = fields.Many2one(
        "library.member", required=True
    )

    user_id = fields.Many2one(
        "res.users", "Libreria",
        default=lambda s: s.env.user
    )

        lines_id = fields.One2many(
        comodel_name='library.checkout.line',
        inverse_name='checkout_id',
        string='Borrowed Books',
        required=False)

    request_date = fields.Date(default=lambda s: fields.Date.today())

