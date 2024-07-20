from odoo import fields, models

class CahngeState(models.TransientModel):
    _name = 'change.state'

    property_id = fields.Many2one('property')
    state = fields.Selection([
        ('draft','Draft'),
        ('pending','Pending'),
    ],default='draft')
    reason = fields.Char()

    def create_history_record(self,old_state,new_state,reason):
        for rec in self:
            rec.env['property.history'].create({
                'user_id' : rec.env.uid,
                'property_id' : rec.id,
                'old_state' : old_state,
                'new_state' : new_state,
                'reason' : reason or "",
            })
    def action_confirm(self):
        if self.property_id.state == 'closed':
            self.property_id.state = self.state
            self.create_history_record('closed',self.state,self.reason)