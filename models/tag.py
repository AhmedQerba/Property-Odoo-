from odoo import fields, models

class Tags(models.Model):
    _name= "tag"

    name = fields.Char()
