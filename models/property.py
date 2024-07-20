from odoo import models, fields,api

class Property(models.Model):
    _name = "property"
    _description = "Property"
    _inherit = ['mail.thread','mail.activity.mixin']

    name = fields.Char(required=True,tracking=1)
    description = fields.Text()
    new_prop = fields.Boolean()
    type = fields.Selection(selection=[('1','new'),('2','old')],tracking=1)
    owner_id = fields.Many2one("owner")
    phone = fields.Integer(related="owner_id.phone")
    tag_ids = fields.Many2many("tag")
    state = fields.Selection([('draft','Draft'),('pending','Pending'),('sold','Sold'),('closed','Closed')])
    expected = fields.Float(store=1)
    price = fields.Float(store=1)
    diff = fields.Float(compute="_diff_price",store=1,tracking=1)
    line_ids = fields.One2many('property.line','property_id')
    active = fields.Boolean(default=True)
    expected_selling_date = fields.Date(tracking=1)
    is_late = fields.Boolean()
    _sql_constraints = [
        ('unique_name','unique("name")','This name is exist!')
    ]
    ref = fields.Char(default='New',readonly=1)

    def action_draft(self):
        for rec in self:
            rec.state = 'draft'
    def action_pending(self):
        for rec in self:
            rec.state = 'pending'
    def action_sold(self):
        for rec in self:
            rec.state = 'sold'
    def action_closed(self):
        for rec in self:
            rec.state = 'closed'
    def expected_date_check(self):
        property_ids = self.search([])
        for rec in property_ids:
            if rec.expected_selling_date and rec.expected_selling_date < fields.date.today():
                rec.is_late = True

    @api.depends('expected','price')
    def _diff_price(self):
        for rec in self:
            rec.diff = rec.expected - rec.price

    @api.onchange('expected','price')
    def _check_price(self):
        for rec in self:
            if rec.expected < 0:
                return {
                    'warning': {'title':'warning', 'message': 'negative value.', 'type': 'notification'}
                }

    @api.model
    def create(self,vals):
        res = super(Property, self).create(vals)
        if res.ref == 'New':
            res.ref = self.env['ir.sequence'].next_by_code('property_seq')
        return res

    def action_open_change_state_wizard(self):
        action = self.env['ir.actions.actions']._for_xml_id('app_one.change_state_wizard_action')
        action['context'] = {'default_property_id': self.id}
        return action

class PropertyLine(models.Model):
    _name = 'property.line'

    property_id = fields.Many2one('property')
    area = fields.Float()
    desc = fields.Char(string='Description')
