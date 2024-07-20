from odoo import fields, models

class Owner(models.Model):
    _name = "owner"

    name = fields.Char(required=True)
    phone = fields.Integer(size=12)
    property_ids = fields.One2many('property','owner_id')