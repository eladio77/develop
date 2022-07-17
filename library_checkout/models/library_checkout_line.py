from odoo import fields, models, api


class Checkoutline(models.Model):
    _name = 'library.checkout.line'
    _description = 'Checkout Line'

    checkout_id = fields.Many2one(
        comodel_name='library.checkout',
        required=True)

    note = fields.Char("Notes")
