from odoo import fields, models

class PropertyHistory(models.Model):
    _name = "property.history"

    user_id = fields.Many2one('res.users')
    property_id = fields.Many2one('property')
    old_state = fields.Char()
    new_state = fields.Char()
    reason = fields.Char()
